from persistor import Persistor
from utils.tickers import Tickers


def main():
    persistor = Persistor()

    tickers = Tickers()

    for ticker in tickers.get_us_tickers():
        dictionary = persistor.read_pickle('pickle', ticker, 'company')
        if dictionary is not None:
            persistor.write_dict_to_json('json/', ticker, 'company', dictionary)
        else:
            print(ticker + ' ' + 'stocks' + ' ' + 'dictionary doesn\'t exits')



if __name__ == '__main__':
    main()