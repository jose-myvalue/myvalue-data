from persistor import Persistor
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.set_option('display.max_columns', 10)

persistor = Persistor()

total_revenue_df = persistor.read_pickle('pickle', 'AAPL', 'totalrevenue')
revenuegrowth_df = persistor.read_pickle('pickle', 'AAPL', 'revenuegrowth')
ebit_df = persistor.read_pickle('pickle', 'AAPL', 'ebit')
ebit_margin_df = persistor.read_pickle('pickle', 'AAPL', 'ebitmargin')
capex_df = persistor.read_pickle('pickle', 'AAPL', 'capex')
depreciationandamortization_df = persistor.read_pickle('pickle', 'AAPL', 'depreciationandamortization')
nwc_df = persistor.read_pickle('pickle', 'AAPL', 'nwc')
nwctorev_df = persistor.read_pickle('pickle', 'AAPL', 'nwctorev')

df_dcf = pd.concat([total_revenue_df, revenuegrowth_df, ebit_df, ebit_margin_df, capex_df, depreciationandamortization_df, nwc_df, nwctorev_df], axis=1)

df_dcf['capex_revenue'] = df_dcf['capex'] / df_dcf['totalrevenue']

df_dcf.sort_index(inplace=True)

#df_dcf_transpose = df_dcf.T

#print(df_dcf_transpose)

df_dcf['changeyonynwc'] = df_dcf['nwc'].pct_change()

print(df_dcf)
