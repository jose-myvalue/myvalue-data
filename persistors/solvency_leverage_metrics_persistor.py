import intrinio_sdk

from utils.tickers import Tickers
from utils.metricnames import MetricNames
from utils.metricscalculator import MetricsCalculator
from utils.persistor import Persistor
from datequarter import DateQuarter

import os.path
from os import path

import pandas as pd

from tqdm import tqdm

pd.set_option('display.max_columns', 30)

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():
    persistor = Persistor()
    start_date = '2010-05-18'
    end_date = '2020-05-18'
    frequency = 'quarterly'

    tickers = Tickers()
    metrics = MetricNames()

    calculator = MetricsCalculator()

    for ticker in tqdm(tickers.get_us_tickers()):
        for metric in metrics.get_solvency_leverage_metrics():
            if path.exists('pickle/' + ticker + '_' + metric + '_solvency_leverage.pkl'):
                metrics_df = persistor.read_pickle('pickle', ticker, metric, 'solvency_leverage')
            else:
                metrics_df = pd.DataFrame()

            if metrics_df.empty:
                metrics_df = calculator.get_company_metrics(ticker, metric, start_date, end_date, frequency)
                if metrics_df is not None:
                    metrics_df.sort_index(inplace=True)
                    persistor.write_pickle('pickle', ticker, metric, metrics_df, 'solvency_leverage')
                else:
                    continue
            else:
                max_date = metrics_df.index.values.max()
                min_date = metrics_df.index.values.min()
                if metric in metrics_df and \
                        ((max_date >= DateQuarter.from_date(pd.to_datetime(start_date)) >=
                          min_date or
                          (min_date <= DateQuarter.from_date(pd.to_datetime(end_date)) <=
                         max_date))):
                    print('me salgo')
                    print(ticker)
                    print(metric)
                    print('min: ' + min_date)
                    print('max: ' + max_date)
                    print('start_date: ' + str(DateQuarter.from_date(pd.to_datetime(start_date)).start_date()))
                    print('end_date: ' + str(DateQuarter.from_date(pd.to_datetime(end_date))))
                    break

                print('oye que he entrado')
                print(ticker)
                print(metric)
                print('min: ' + min_date)
                print('max: ' + max_date)
                print('start_date: ' + str(DateQuarter.from_date(pd.to_datetime(start_date))))
                print('end_date: ' + str(DateQuarter.from_date(pd.to_datetime(end_date))))
                metrics_new_df = calculator.get_company_metrics(ticker, metric, start_date, end_date, frequency)
                metrics_result_df = pd.concat([metrics_df, metrics_new_df])
                metrics_result_df.sort_index(inplace=True)
                persistor.write_pickle('pickle', ticker, metric, metrics_result_df, 'solvency_leverage')


if __name__ == '__main__':
    main()
