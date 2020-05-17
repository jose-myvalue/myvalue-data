from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'

#https://docs.intrinio.com/documentation/python/get_fundamental_standardized_financials_v2

fundamentals_api = intrinio_sdk.FundamentalsApi()

id = 'AAPL-income_statement-2016-Q4' # str | The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental

try:
  api_response = fundamentals_api.get_fundamental_standardized_financials(id)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling FundamentalsApi->get_fundamental_standardized_financials: %s\r\n" % e)