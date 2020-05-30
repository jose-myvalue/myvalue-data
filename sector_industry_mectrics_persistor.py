import pickle
import pandas as pd
import numpy as np

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from persistor import Persistor
from utils.tickers import Tickers
from utils.metricnames import MetricNames


def get_valuation_means_by_group(group_dict):
    persistor = Persistor()
    metrics = MetricNames()
    for industry in group_dict:
        print('Industry: ' + industry)
        for metric in metrics.get_industry_comparation_metrics():
            print('\tmetric: ' + metric)
            industry_group_dataframes_list = list()
            for company in group_dict[industry]:
                print('\t\tcompany: ' + company)
                company_valuation_metrics_df = persistor.read_pickle('pickle', company, metric)
                per = company_valuation_metrics_df[metric]
                print(per.head(1))
                industry_group_dataframes_list.append(per)
            try:
                df_concat = pd.concat(industry_group_dataframes_list)
                df_concat.fillna(value=np.nan, inplace=True)
                by_row_index = df_concat.groupby(df_concat.index)
                df_means = by_row_index.mean()
                print('\tDF Means')
                print(df_means.tail(1))
                persistor.write_pickle('pickle', industry, metric, df_means)
            except ValueError:
                print('no data for ' + metric)
                print(group_dict[industry])


def get_grouped_companies(group_set, companies_dict):
    tickers = Tickers()
    group_dict = dict()

    for group in group_set:
        group_list = list()
        for ticker in tickers.get_us_tickers():
            ig = companies_dict[ticker]['industry_group'].replace('/', '-').replace(' ', '-').replace(',', '').lower() #TODO still need to change this for sector and industry category
            if ig == group:
                group_list.append(companies_dict[ticker]['ticker'])
        group_dict[group] = group_list
    return group_dict


def main():
    persistor = Persistor()
    tickers = Tickers()

    sector_set = set()
    industry_category_set = set()
    industry_group_set = set()

    companies_dict = dict()

    for ticker in tickers.get_us_tickers():
        company_dict = persistor.read_pickle('pickle', ticker, 'company')
        companies_dict[ticker] = company_dict

        sector_set.add(company_dict['sector'].replace('/', '-').replace(' ', '-').replace(',', '').lower())
        industry_category_set.add(company_dict['industry_category'].replace('/', '-').replace(' ', '-').replace(',', '').lower())
        industry_group_set.add(company_dict['industry_group'].replace('/', '-').replace(' ', '-').replace(',', '').lower())

    print('------------------------------------------------------------------------INDUSTRY GROUP')
    industry_group_dict = get_grouped_companies(industry_group_set, companies_dict)
    get_valuation_means_by_group(industry_group_dict)

    print('-----------------------------------------------------------------------------SECTOR')
    sector_dict = get_grouped_companies(sector_set, companies_dict)
    get_valuation_means_by_group(sector_dict)

    print('------------------------------------------------------------------------INDUSTRY CATEGORY')
    industry_category_dict = get_grouped_companies(industry_category_set, companies_dict)
    get_valuation_means_by_group(industry_category_dict)


if __name__ == '__main__':
    main()