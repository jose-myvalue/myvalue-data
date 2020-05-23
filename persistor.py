import json
from fastparquet import write
import pickle
import os


class Persistor:

    @staticmethod
    def write_dataframe_to_json_daily_basis(path, ticker, metric, df, id='_'):
        try:
            df.reset_index(inplace=True)
            df['date'] = df['date'].dt.strftime('%Y-%m-%d')
            df.set_index('date', inplace=True)
            df = df.loc[~df.index.duplicated(keep='last')]
            df.to_json(path + ticker + '_' + metric + '_' + id + '.json')
        except AttributeError as e:
            print(ticker + ' ' + metric + ' ' + 'dataframe empty')
            print(str(e))

    @staticmethod
    def write_dataframe_to_json_quarterly_basis(path, ticker, metric, df, id='_'):
        try:
            df.reset_index(inplace=True)
            df.set_index('date', inplace=True)
            df = df.loc[~df.index.duplicated(keep='last')]
            df.to_json(path + ticker + '_' + metric + '_' + id + '.json')
        except AttributeError as e:
            print(ticker + ' ' + metric + ' ' + 'dataframe empty')

    @staticmethod
    def write_dict_to_json(path, ticker, metric, dictionary, id='_'):
        file_name = str(path + '/' + ticker + '_' + metric + '_' + id + '.json')
        file = open(file_name, 'w+')
        json.dump(dictionary, file)
        file.close()


    @staticmethod
    def write_pickle(path, ticker, metric, df, id):
        file_name = str(path + '/' + ticker + '_' + metric + '_' + id + '.pkl')
        file = open(file_name, 'wb')
        pickle.dump(df, file)
        file.close()

    @staticmethod
    def read_pickle(path, ticker, metric, id='_'):
        try:
            file_name = str(path + '/' + ticker + '_' + metric + '_' + id + '.pkl')
            file = open(file_name, 'rb')
            df = pickle.load(file)
            file.close()
            return df
        except FileNotFoundError as e:
            print(str(e))
