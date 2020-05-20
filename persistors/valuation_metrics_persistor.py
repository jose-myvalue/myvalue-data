import intrinio_sdk

from utils.tickers import Tickers
from utils.metricnames import MetricNames
from utils.metricscalculator import MetricsCalculator
from utils.persistor import Persistor
import pickle

import os
import os.path
from os import path

import pandas as pd
import numpy as np

from tqdm import tqdm

pd.set_option('display.max_columns', 30)

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():
    persistor = Persistor()
    start_date = '2020-05-18'
    end_date = '2020-04-01'
    frequency = 'daily'

    tickers = Tickers()
    metrics = MetricNames()

    calculator = MetricsCalculator()

    for ticker in tqdm(tickers.get_us_tickers()):
        for metric in metrics.get_valuation_metrics_names():
            if path.exists('pickle/' + ticker + '_' + metric + '_valuation.pkl'):
                metrics_df = persistor.read_pickle('pickle', ticker, metric, 'valuation')
            else:
                metrics_df = pd.DataFrame()

            if metrics_df.empty:
                metrics_df = calculator.get_company_metrics(ticker, metric, start_date, end_date, frequency)
                metrics_df.sort_index(inplace=True)
                persistor.write_pickle('pickle', ticker, metric, metrics_df, 'valuation')
            else:
                max_date = pd.to_datetime(metrics_df.index.values.max())
                min_date = pd.to_datetime(metrics_df.index.values.min())
                if metric in metrics_df and \
                        ((max_date >= pd.to_datetime(start_date) >=
                          min_date or \
                        (min_date <= pd.to_datetime(end_date) <=
                         max_date))):
                    break

                print('viejo')
                print(metrics_df)
                metrics_new_df = calculator.get_company_metrics(ticker, metric, start_date, end_date, frequency='daily')
                print('nuevo')
                print(metrics_new_df)
                metrics_result_df = pd.concat([metrics_df, metrics_new_df])
                metrics_result_df.sort_index(inplace=True)
                print(metrics_result_df.dtypes)
                print(metrics_result_df)
                persistor.write_pickle('pickle', ticker, metric, metrics_result_df, 'valuation')
        break


if __name__ == '__main__':
    main()