import intrinio_sdk
from utils.companies import Companies
from utils.company import Company
import json

#https://data.intrinio.com/data-tags/calculations-metrics

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'


def main():
    companies_profile_file = open('json/companies_profiles.json', 'w+')

    companies = Companies()
    tickers = companies.get_us_tickers()
    company = Company()

    companies_profile_list = list()

    for ticker in tickers:
        company_profile_dict = company.get_company_info(ticker)
        companies_profile_list.append(company_profile_dict)

    json.dump(companies_profile_list, companies_profile_file)

    companies_profile_file.close()


if __name__ == '__main__':
    main()