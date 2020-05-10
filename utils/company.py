import intrinio_sdk
from intrinio_sdk.rest import ApiException


class Company:

    def get_company_info(self, ticker):

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