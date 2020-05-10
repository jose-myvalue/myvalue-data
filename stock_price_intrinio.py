from __future__ import print_function
import intrinio_sdk
from utils.stocks import Stocks
from utils.my_value_json import MyValueJson
from utils.companies import Companies

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'


def main():

    path = 'json'
    my_value_json = MyValueJson()

    companies = Companies()
    tickers = companies.get_us_tickers()

    stock = Stocks()

    for ticker in tickers:
        price_list = stock.get_close_price(ticker)
        my_value_json.to_json(path, ticker, price_list, 'stock_prices')


if __name__ == '__main__':
    main()
