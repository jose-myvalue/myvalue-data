import intrinio_sdk
from intrinio_sdk.rest import ApiException
from intrinio_sdk.models.company import Company
import os
import pandas as pd
import pickle
import json

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API

security_api = intrinio_sdk.SecurityApi()

ticker = 'AAPL'

identifier = ticker  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)

try:
    company_api = intrinio_sdk.CompanyApi()
    company = company_api.get_company(identifier)
    company_dict = dict()
    company_dict['business_address'] = company.business_address
    company_dict['ceo'] = company.ceo
    company_dict['company_url'] = company.company_url
    company_dict['employees'] = company.employees
    company_dict['hq_address_city'] = company.hq_address_city
    company_dict['hq_address_postal_code'] = company.hq_address_postal_code
    company_dict['hq_country'] = company.hq_country
    company_dict['hq_state'] = company.hq_state
    company_dict['industry_category'] = company.industry_category
    company_dict['industry_group'] = company.industry_group
    company_dict['legal_name'] = company.legal_name
    company_dict['name'] = company.name
    company_dict['sector'] = company.sector
    company_dict['short_description'] = company.short_description
    company_dict['stock_exchange'] = company.stock_exchange
    company_dict['ticker'] = company.ticker

    with open('../json/aapl_company_profile.json', 'w') as fp:
        json.dump(company_dict, fp)


except ApiException as e:
    print("Exception when calling CompanyApi->get_company: %s\n" % e)