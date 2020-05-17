import intrinio_sdk
from intrinio_sdk.rest import ApiException


class Company:
    @staticmethod
    def get_company_info(ticker):

        identifier = ticker  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)

        try:
            company_api = intrinio_sdk.CompanyApi()
            api_response = company_api.get_company(identifier)

            company_profile_dict = dict()
            company_name_list = list()
            stock_exchange_list = list()
            company_name_list.append(api_response.name)
            stock_exchange_list.append(api_response.stock_exchange)
            company_profile_dict["company_name"] = company_name_list
            company_profile_dict['stock_exchange'] = stock_exchange_list

            return company_profile_dict

        except ApiException as e:
            print("Exception when calling CompanyApi->get_company: %s\n" % e)