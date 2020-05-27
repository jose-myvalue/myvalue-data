import json
from fastparquet import write
import pickle
import os


class Persistor:

    @staticmethod
    def write_dataframe_to_json_daily_basis(directory, ticker, metric, df):
        try:
            df.reset_index(inplace=True)
            df['date'] = df['date'].dt.strftime('%Y-%m-%d')
            df.set_index('date', inplace=True)
            df = df.loc[~df.index.duplicated(keep='last')]
            df.to_json(directory + ticker + '_' + metric + '.json')
        except AttributeError as e:
            print(ticker + ' ' + metric + ' ' + 'dataframe empty')
            print(str(e))

    @staticmethod
    def write_dataframe_to_json_quarterly_basis(directory, ticker, metric, df):
        try:
            df.reset_index(inplace=True)
            df.set_index('date', inplace=True)
            df = df.loc[~df.index.duplicated(keep='last')]
            df.to_json(directory + ticker + '_' + metric + '.json')
        except AttributeError as e:
            print(ticker + ' ' + metric + ' ' + 'dataframe empty')

    @staticmethod
    def write_dict_to_json(directory, ticker, metric, dictionary):
        file_name = str(directory + '/' + ticker + '_' + metric + '.json')
        file = open(file_name, 'w+')
        json.dump(dictionary, file)
        file.close()


    @staticmethod
    def write_pickle(directory, ticker, metric, df):
        file_name = str(directory + '/' + ticker + '_' + metric + '.pkl')
        with open(file_name, 'wb') as handle:
            pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def read_pickle(directory, ticker, metric):
        try:
            file_name = str(directory + '/' + ticker + '_' + metric + '.pkl')
            file = open(file_name, 'rb')
            df = pickle.load(file)
            file.close()
            return df
        except FileNotFoundError as e:
            print(str(e))
