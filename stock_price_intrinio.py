from __future__ import print_function
import intrinio_sdk
from utils.stocks import Stocks
from persistor import Persistor
from utils.tickers import Tickers
import os

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API

def main():

    path = 'json'
    my_value_json = Persistor()

    tickers = Tickers()

    stock = Stocks()

    for ticker in tickers.get_us_tickers():
        price_list = stock.get_close_price(ticker)
        my_value_json.write_json(path, ticker, price_list, 'stock_prices')


if __name__ == '__main__':
    main()
