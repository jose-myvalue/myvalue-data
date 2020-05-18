import json
from fastparquet import write
import pickle


class Persistor:

    @staticmethod
    def write_json(path, ticker, object, id='_'):
        file_name = str(path + '/' + ticker + '_' + id + '.json')
        file = open(file_name, 'w+')

        json.dump(object, file)

        file.close()

    @staticmethod
    def write_pickle(path, ticker, metric, df, id):
        file_name = str(path + '/' + ticker + '_' + metric + '_' + id + '.pkl')
        file = open(file_name, 'wb')
        pickle.dump(df, file)
        file.close()

    @staticmethod
    def read_parquet(path, ticker, metric, id='_'):
        file_name = str(path + '/' + ticker + '_' + metric + '_' + id + '.pkl')
        file = open(file_name, 'rb')
        df = pickle.load(file)
        file.close()
        return df
