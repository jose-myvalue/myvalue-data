from __future__ import print_function
import os
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API

index_api = intrinio_sdk.IndexApi()

page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
  api_response = index_api.get_all_sic_indices(page_size=page_size, next_page=next_page)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling IndexApi->get_all_sic_indices: %s\r\n" % e)