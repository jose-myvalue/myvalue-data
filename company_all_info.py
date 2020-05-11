import intrinio_sdk

from utils.tickers import Tickers
from utils.company import Company
from utils.fundamentals import Fundamentals
from utils.stocks import Stocks
from utils.my_value_json import MyValueJson

import os
from tqdm import tqdm

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():
    metrics = ['ebit', 'freecashflow', 'altmanzscore']

    path = 'json'
    my_value_json = MyValueJson()

    tickers = Tickers()

    company = Company()
    fundamentals = Fundamentals()
    stock = Stocks()

    for ticker in tqdm(tickers.get_us_tickers()):
        company_all_info_list = list()
        company_profile_dict = company.get_company_info(ticker)
        company_all_info_list.append(company_profile_dict)
        for metric in tqdm(metrics):
            metric_dict = fundamentals.get_company_metric(ticker, metric)
            company_all_info_list.append(metric_dict)

        price_list = stock.get_close_price(ticker)
        company_all_info_list.append(price_list)

        my_value_json.to_json(path, ticker, company_all_info_list, 'all')


if __name__ == '__main__':
    main()