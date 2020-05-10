from __future__ import print_function
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

import json

import pandas as pd

pd.set_option('display.float_format', lambda x: '%.1f' % x)

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'


def get_company_metric(ticker, metric):
    identifier = ticker  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
    tag = metric  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]
    frequency = 'quarterly'  # str | Return historical data in the given frequency (optional) (default to daily)
    type = ''  # str | Return historical data for given fiscal period type (optional)
    start_date = '2010-01-01'  # date | Return historical data on or after this date (optional)
    end_date = ''  # date | Return historical data on or before this date (optional)
    sort_order = 'desc'  # str | Sort by date `asc` or `desc` (optional) (default to desc)
    page_size = 100  # int | The number of results to return (optional) (default to 100)
    next_page = ''  # str | Gets the next page of data from a previous API call (optional)

    try:
        company_api = intrinio_sdk.CompanyApi()
        api_response = company_api.get_company_historical_data(identifier, tag, frequency=frequency, type=type,
                                                           start_date=start_date, end_date=end_date,
                                                           sort_order=sort_order, page_size=page_size,
                                                           next_page=next_page)

        metric_list = list()
        for metric_date_value in api_response.historical_data:
            date_value_dict = {"date": str(metric_date_value.date), "value": str(metric_date_value.value)}
            metric_list.append(date_value_dict)

        metric_dict = dict()
        metric_dict[metric] = metric_list

        company_dict = dict()
        company_dict[ticker] = metric_dict
        return company_dict

    except ApiException as e:
        print("Exception when calling CompanyApi->get_company_historical_data: %s\r\n" % e)


def get_company_info(ticker):

    identifier = ticker  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)

    try:
        company_api = intrinio_sdk.CompanyApi()
        api_response = company_api.get_company(identifier)

        company_profile_dict = dict()
        company_profile_dict["company_name"] = api_response.name
        company_profile_dict['stock_exchange'] = api_response.stock_exchange

        company_dict = dict()
        company_dict[ticker] = company_profile_dict
        return company_dict

    except ApiException as e:
        print("Exception when calling CompanyApi->get_company: %s\n" % e)


def main():
    tickers = ['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'GE', 'GS', 'HD', 'IBM', 'INTC',
               'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UNH', 'UTX',
               'V', 'VZ', 'WMT', 'XOM']

    companies_ebit_file = open('companies_ebit.json', 'w+')
    company_profile_file = open('companies_profile.json', 'w+')

    companies_list = list()
    companies_dict = dict()

    companies_ebit_list = list()
    companies_ebit_dict = dict()

    for ticker in tickers:
        ebit_dict = get_company_metric(ticker, 'ebit')
        company_dict = get_company_info(ticker)

        companies_list.append(company_dict)
        companies_ebit_list.append(ebit_dict)

        companies_dict['companies'] = companies_list
        companies_ebit_dict['companies'] = companies_ebit_list

    json.dump(companies_dict, company_profile_file)
    json.dump(companies_ebit_dict, companies_ebit_file)

    company_profile_file.close()
    companies_ebit_file.close()


if __name__ == '__main__':
    main()
