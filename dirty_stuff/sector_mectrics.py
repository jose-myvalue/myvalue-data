import pickle
import pandas as pd

from persistor import Persistor
from utils.tickers import Tickers

persistor = Persistor()
tickers = Tickers()

market_df = pd.DataFrame()
sector_set = set()
industry_category_set = set()
industry_group_set = set()

companies_dict = dict()
companies_valuation_dict = dict()

for ticker in tickers.get_us_tickers():
    company_dict = persistor.read_pickle('../pickle', ticker, 'company', 'profile')
    company_valuation_metrics_df = persistor.read_pickle('../pickle', ticker, 'pricetoearnings', 'valuation')
    companies_dict[ticker] = company_dict
    companies_valuation_dict = company_valuation_metrics_df

    sector_set.add(company_dict['sector'])
    industry_category_set.add(company_dict['industry_category'])
    industry_group_set.add(company_dict['industry_group'])

industry_group_dict = dict()

for industry_group in industry_group_set:
    industry_group_list = list()
    for ticker in tickers.get_us_tickers():
        if companies_dict[ticker]['industry_group'] == industry_group:
            industry_group_list.append(companies_dict[ticker]['ticker'])
    industry_group_dict[industry_group] = industry_group_list

print(industry_group_dict)

for i in industry_group_dict:
    print(i)
    for c in industry_group_dict[i]:
        print('\t' + c)
        company_valuation_metrics_df = persistor.read_pickle('../pickle', c, 'pricetoearnings', 'valuation')
        print('\tPER: ' + str(company_valuation_metrics_df.loc[company_valuation_metrics_df.index.max()]['pricetoearnings']))


