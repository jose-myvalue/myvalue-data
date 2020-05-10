import intrinio_sdk
from utils.companies import Companies
from utils.company import Company
from utils.my_value_json import MyValueJson

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'


def main():

    path = 'json'
    my_value_json = MyValueJson()

    companies = Companies()
    tickers = companies.get_us_tickers()

    company = Company()

    for ticker in tickers:
        company_profile_dict = company.get_company_info(ticker)
        my_value_json.to_json(path, ticker, company_profile_dict, 'profile')


if __name__ == '__main__':
    main()