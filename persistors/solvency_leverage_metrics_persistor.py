import intrinio_sdk

from utils.tickers import Tickers
from utils.metricnames import MetricNames
from utils.metricscalculator import MetricsCalculator
from utils.persistor import Persistor

import pandas as pd

import os
from tqdm import tqdm

pd.set_option('display.max_columns', 30)

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():
    start_date = '2010-01-01'
    end_date = '2020-05-15'

    tickers = Tickers()
    metrics = MetricNames()

    calculator = MetricsCalculator()

    for ticker in tqdm(tickers.get_us_tickers()):
        metrics_df = pd.DataFrame()
        #for metric in metrics.get_valuation_metrics_names():
        for metric in metrics.get_solvency_leverage_metrics():
            if metrics_df.empty:
                metrics_df = calculator.get_company_metrics(ticker, metric, start_date, end_date, frequency='quarterly')
            else:
                metrics_df = pd.merge(metrics_df,
                                      calculator.get_company_metrics(ticker, metric, start_date, end_date, frequency='quarterly'),
                                      on='date',
                                      how='outer')

        metrics_df.sort_index(inplace=True)
        print(metrics_df)

        break


if __name__ == '__main__':
    main()