import intrinio_sdk

from datetime import datetime

from utils.tickers import Tickers
from utils.stocks import Stocks
from persistor import Persistor

import os.path

import pandas as pd

from tqdm import tqdm

pd.set_option('display.max_columns', 30)

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():
    persistor = Persistor()
    start_date = '2020-03-18'
    end_date = datetime.now()
    frequency = 'daily'

    tickers = Tickers()

    calculator = Stocks()

    for ticker in tqdm(tickers.get_us_tickers()):
        stock_df = calculator.get_stock_prices(ticker, start_date, end_date, frequency)
        persistor.write_pickle('pickle', ticker, 'stocks', stock_df, 'prices')


if __name__ == '__main__':
    main()