from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'

index_api = intrinio_sdk.IndexApi()

identifier = '$SIC.70'  # str | An Index Identifier (symbol, Intrinio ID)
tag = 'pricetoearnings'  # str | An Intrinio data tag ID or code-name
type = ''  # str | Filter by type, when applicable (optional)
start_date = '2018-01-01'  # date | Get historical data on or after this date (optional)
end_date = ''  # date | Get historical data on or before this date (optional)
sort_order = 'desc'  # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100  # int | The number of results to return (optional) (default to 100)
next_page = ''  # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_sic_index_historical_data(identifier, tag, type=type, start_date=start_date,
                                                           end_date=end_date, sort_order=sort_order,
                                                           page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_sic_index_historical_data: %s\r\n" % e)
