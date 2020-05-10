from __future__ import print_function
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

import json

import pandas as pd

pd.set_option('display.float_format', lambda x: '%.1f' % x)

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'

tickers = ['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'GE', 'GS', 'HD', 'IBM', 'INTC',
           'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UNH', 'UTX',
           'V', 'VZ', 'WMT', 'XOM']

company_api = intrinio_sdk.CompanyApi()

final_ebit_df = pd.DataFrame()

file = open('ebit.json', 'w+')

try:

    companies_dict = dict()
    companies_list = list()

    for ticker in tickers:
        print(ticker)
        identifier = ticker  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
        tag = 'ebit'  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]
        frequency = 'quarterly'  # str | Return historical data in the given frequency (optional) (default to daily)
        type = ''  # str | Return historical data for given fiscal period type (optional)
        start_date = '2010-01-01'  # date | Return historical data on or after this date (optional)
        end_date = ''  # date | Return historical data on or before this date (optional)
        sort_order = 'desc'  # str | Sort by date `asc` or `desc` (optional) (default to desc)
        page_size = 100  # int | The number of results to return (optional) (default to 100)
        next_page = ''  # str | Gets the next page of data from a previous API call (optional)

        api_response = company_api.get_company_historical_data(identifier, tag, frequency=frequency, type=type,
                                                               start_date=start_date, end_date=end_date,
                                                               sort_order=sort_order, page_size=page_size,
                                                               next_page=next_page)

        #pprint(api_response)
        ebit_list = list()
        for ebit in api_response.historical_data:
            date_value_dict = {"date": str(ebit.date), "value": str(ebit.value)}
            ebit_list.append(date_value_dict)

        ebit_dict = dict()
        ebit_dict["ebit"] = ebit_list

        company_name_dict = dict()
        company_name_dict["company_name"] = api_response.company.name

        data_list = list()
        data_list.append(company_name_dict)
        data_list.append(ebit_dict)

        company_dict = dict()
        company_dict[api_response.company.ticker] = data_list

        companies_list.append(company_dict)

        ebit_df = pd.DataFrame(api_response.historical_data_dict)
        ebit_df['company_name'] = api_response.company.name
        ebit_df['ticker'] = api_response.company.ticker
        ebit_df.rename(columns={'value':'ebit'}, inplace=True)

        final_ebit_df = final_ebit_df.append(ebit_df, ignore_index=True)

    companies_dict['companies'] = companies_list

    json.dump(companies_dict, file)

    file.close()

except ApiException as e:
        print("Exception when calling CompanyApi->get_company_historical_data: %s\r\n" % e)

