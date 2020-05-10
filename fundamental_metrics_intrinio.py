import intrinio_sdk
from companies import Companies
from metrics.fundamentals import Fundamentals
import json

#https://data.intrinio.com/data-tags/calculations-metrics

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'

def main():
    companies_ebit_file = open('json/companies_ebit.json', 'w+')

    companies = Companies()
    tickers = companies.get_us_tickers()
    fundamentals = Fundamentals()

    companies_ebit_list = list()

    for ticker in tickers:
        ebit_dict = fundamentals.get_company_metric(ticker, 'ebit')
        companies_ebit_list.append(ebit_dict)

    json.dump(companies_ebit_list, companies_ebit_file)

    companies_ebit_file.close()


if __name__ == '__main__':
    main()
