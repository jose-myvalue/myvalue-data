from persistor import Persistor
from utils.tickers import Tickers
from utils.metricnames import MetricNames


def main():
    persistor = Persistor()

    tickers = Tickers()

    for ticker in tickers.get_us_tickers():
        df = persistor.read_pickle('pickle', ticker, 'stocks', 'prices')
        if df is not None:
            persistor.write_json_daily_basis('json/', ticker, 'stock', df, 'prices')
        else:
            print(ticker + ' ' + 'stocks' + ' ' + 'dataframe doesn\'t exits')



if __name__ == '__main__':
    main()
