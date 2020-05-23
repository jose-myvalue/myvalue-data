import intrinio_sdk
from utils.company import Company
from persistor import Persistor
import os
import json
from tqdm import tqdm

from utils.tickers import Tickers

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():

    tickers = Tickers()
    company = Company()

    persistor = Persistor()

    for ticker in tqdm(tickers.get_us_tickers()):
        company_profile_dict = company.get_company_info(ticker)
        persistor.write_pickle('pickle', ticker, 'company', company_profile_dict, 'profile')

if __name__ == '__main__':
    main()