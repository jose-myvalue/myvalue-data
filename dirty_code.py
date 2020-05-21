#import pickle
#import pandas as pd

#def read_pickle(path, ticker, metric, id='_'):
#    file_name = str('../' + path + '/' + ticker + '_' + metric + '_' + id + '.pkl')
#    print(file_name)
#    file = open(file_name, 'rb')
#    try:
#        file_name = str(path + '/' + ticker + '_' + metric + '_' + id + '.pkl')
#        file = open(file_name, 'rb')
#        df = pickle.load(file)
#        file.close()
#        return df
#    except FileNotFoundError as e:
#        print(str(e))

#file_name = 'pickle/AAPL_dividendyield_valuation.pkl'
#file = open(file_name, 'rb')
#df = pickle.load(file)

#print(df.head())

import os
my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
print(my_absolute_dirpath)

file = open('pickle/borrar.pkl', 'w+')
