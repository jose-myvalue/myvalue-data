import intrinio_sdk

from datetime import datetime

from utils.tickers import Tickers
from utils.metricnames import MetricNames
from utils.metrics import Metrics
from persistor import Persistor

import os.path

import pandas as pd

from tqdm import tqdm

pd.set_option('display.max_columns', 30)

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():
    persistor = Persistor()
    start_date = '2010-05-18'
    end_date = datetime.now()
    frequency = 'quarterly'

    tickers = Tickers()
    metrics = MetricNames()

    calculator = Metrics()

    for ticker in tqdm(tickers.get_us_tickers()):
        for metric in metrics.get_liquidity_metrics():
            metrics_df = calculator.get_company_metrics(ticker, metric, start_date, end_date, frequency)
            persistor.write_pickle('pickle', ticker, metric, metrics_df, 'liquidity')


if __name__ == '__main__':
    main()
