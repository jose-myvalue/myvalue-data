import intrinio_sdk
from intrinio_sdk.rest import ApiException
import os
import pandas as pd

INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API

security_api = intrinio_sdk.SecurityApi()

ticker = 'AAPL'

identifier = ticker  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
start_date = '2020-03-01'  # date | Return prices on or after the date (optional)
end_date = '2020-05-10'  # date | Return prices on or before the date (optional)
frequency = 'daily'  # str | Return stock prices in the given frequency (optional) (default to daily)
page_size = 100  # int | The number of results to return (optional) (default to 100)
next_page = ''  # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = security_api.get_security_stock_prices(identifier, start_date=start_date, end_date=end_date,
                                                          frequency=frequency, page_size=page_size,
                                                          next_page=next_page)

    df = pd.DataFrame(api_response.stock_prices_dict)

    print(df.head())

except ApiException as e:\
    print("Exception when calling SecurityApi->get_security_stock_prices: %s\r\n" % e)