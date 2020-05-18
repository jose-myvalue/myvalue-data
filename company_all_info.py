import intrinio_sdk

from utils.tickers import Tickers
from utils.metricnames import MetricNames
from utils.company import Company
from utils.metricscalculator import MetricsCalculator
from utils.stocks import Stocks
from utils.persistor import Persistor

import pandas as pd

import os
from tqdm import tqdm

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():

    path = 'json'
    my_value_json = Persistor()

    tickers = Tickers()
    metrics = MetricNames()

    company = Company()
    fundamentals = MetricsCalculator()
    stock = Stocks()

    for ticker in tqdm(tickers.get_us_tickers()):
        company_dict = dict()
        company_dict['company_profile'] = company.get_company_info(ticker)
        company_profile_df = pd.DataFrame(company_dict['company_profile'])
        metrics_df = pd.DataFrame()
        for metric in metrics.get_valuation_metrics_names():
            if metrics_df.empty:
                metrics_df = fundamentals.get_company_metrics(ticker, metric, frequency='yearly')
            else:
                metrics_df = pd.merge(metrics_df, fundamentals.get_company_metrics(ticker, metric, frequency='yearly'), on='date')


        print(metrics_df)

        price_list = stock.get_close_price(ticker)
        company_dict['stock_prices'] = price_list

        my_value_json.write_json(path, ticker, company_dict, 'all')
        break


if __name__ == '__main__':
    main()