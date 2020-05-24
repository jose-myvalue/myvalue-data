import intrinio_sdk
from utils.company import Company
from persistor import Persistor
import os
from tqdm import tqdm
from time import time

from queue import Queue
from threading import Thread

from utils.tickers import Tickers

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            ticker = self.queue.get()
            try:
                persistor = Persistor()
                company = Company()
                company_profile_dict = company.get_company_info(ticker)
                persistor.write_pickle('pickle', ticker, 'company', company_profile_dict, 'profile')
            finally:
                self.queue.task_done()


def main():
    ts = time()

    tickers = Tickers()
    queue = Queue()

    for x in range(5):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()

    for ticker in tqdm(tickers.get_us_tickers()):
        queue.put(ticker)

    queue.join()
    print(time() - ts)


if __name__ == '__main__':
    main()