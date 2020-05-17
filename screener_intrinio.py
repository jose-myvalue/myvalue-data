from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'

security_api = intrinio_sdk.SecurityApi()

identifier = 'AAPL'  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
tag = 'freecashflow'  # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)
frequency = 'daily'  # str | Return historical data in the given frequency (optional) (default to daily)
type = ''  # str | Filter by type, when applicable (optional)
start_date = '2015-01-01'  # date | Get historical data on or after this date (optional)
end_date = '2020-05-15'  # date | Get historical date on or before this date (optional)
sort_order = 'desc'  # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100  # int | The number of results to return (optional) (default to 100)
next_page = ''  # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = security_api.get_security_historical_data(identifier, tag, frequency=frequency, type=type,
                                                             start_date=start_date, end_date=end_date,
                                                             sort_order=sort_order, page_size=page_size,
                                                             next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_security_historical_data: %s\n" % e)

# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict)