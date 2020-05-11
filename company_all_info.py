import intrinio_sdk

from utils.tickers import Tickers
from utils.metrics import Metrics
from utils.company import Company
from utils.fundamentals import Fundamentals
from utils.stocks import Stocks
from utils.my_value_json import MyValueJson

import os
from tqdm import tqdm

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():

    path = 'json'
    my_value_json = MyValueJson()

    tickers = Tickers()
    metrics = Metrics()

    company = Company()
    fundamentals = Fundamentals()
    stock = Stocks()

    for ticker in tqdm(tickers.get_us_tickers()):
        company_dict = dict()
        company_dict['company_profile'] = company.get_company_info(ticker)
        for metric in tqdm(metrics.get_value_metrics()):
            metric_dict = fundamentals.get_company_metric(ticker, metric)
            company_dict[metric] = metric_dict

        price_list = stock.get_close_price(ticker)
        company_dict['stock_prices'] = price_list

        my_value_json.to_json(path, ticker, company_dict, 'all')


if __name__ == '__main__':
    main()