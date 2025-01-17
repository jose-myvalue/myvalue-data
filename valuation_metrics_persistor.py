import intrinio_sdk

from utils.tickers import Tickers
from utils.metricnames import MetricNames
from utils.metrics import Metrics
from persistor import Persistor

from datetime import datetime

from time import time

import os.path
from os import path

import pandas as pd

from queue import Queue
from threading import Thread

from tqdm import tqdm

pd.set_option('display.max_columns', 30)

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            ticker, metric, start_date, end_date, frequency = self.queue.get()
            try:
                persistor = Persistor()
                calculator = Metrics()
                metrics_df = calculator.get_company_metrics(ticker, metric, start_date, end_date, frequency)
                persistor.write_pickle('pickle', ticker, metric, metrics_df)
            finally:
                self.queue.task_done()


def main():
    ts = time()
    start_date = '2020-03-20'
    end_date = datetime.now()
    frequency = 'daily'

    tickers = Tickers()
    metrics = MetricNames()

    queue = Queue()

    for x in range(6):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()

    for ticker in tqdm(tickers.get_us_tickers()):
        for metric in metrics.get_valuation_metrics_names():
            queue.put((ticker, metric, start_date, end_date, frequency))

    queue.join()

    print(time() - ts)


if __name__ == '__main__':
    main()