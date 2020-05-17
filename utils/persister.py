import json


class Persister:

    @staticmethod
    def to_json(path, ticker, object, id='_'):
        file_name = str(path + '/' + ticker + '_' + id + '.json')
        file = open(file_name, 'w+')

        json.dump(object, file)

        file.close()

    @staticmethod
    def to_dataframe():
        pass