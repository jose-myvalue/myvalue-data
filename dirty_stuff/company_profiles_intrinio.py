import intrinio_sdk
from utils.tickers import Tickers
from utils.company import Company
from persistor import Persistor
import os

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():

    path = '../json'
    my_value_json = Persistor()

    tickers = Tickers()

    company = Company()

    for ticker in tickers.get_us_tickers():
        company_profile_dict = company.get_company_info(ticker)
        my_value_json.write_json(path, ticker, company_profile_dict, 'profile')


if __name__ == '__main__':
    main()