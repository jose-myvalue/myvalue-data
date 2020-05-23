import intrinio_sdk
from intrinio_sdk.rest import ApiException
from datequarter import DateQuarter

import pandas as pd


class Stocks:

    @staticmethod
    def get_stock_prices(ticker, start_date, end_date, frequency='daily', next_page=''):
        security_api = intrinio_sdk.SecurityApi()

        identifier = ticker  # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
        start_date = start_date  # date | Return prices on or after the date (optional)
        end_date = end_date  # date | Return prices on or before the date (optional)
        frequency = frequency  # str | Return stock prices in the given frequency (optional) (default to daily)
        page_size = 100  # int | The number of results to return (optional) (default to 100)
        next_page = next_page  # str | Gets the next page of data from a previous API call (optional)

        try:
            api_response = security_api.get_security_stock_prices(identifier, start_date=start_date, end_date=end_date,
                                                                  frequency=frequency, page_size=page_size,
                                                                  next_page=next_page)

            df = pd.DataFrame(api_response.stock_prices_dict)
            if not df.empty:
                #df.rename(columns={"value": metric}, inplace=True)
                if frequency == 'yearly':
                    df.reset_index('date', inplace=True)
                    df['date'] = df['date'].apply(lambda x: x.year)
                    df.set_index('date', inplace=True)
                elif frequency == 'quarterly':
                    df['date'] = df['date'].apply(lambda x: DateQuarter.from_date(x))
                    df.set_index('date', inplace=True)
                elif frequency == 'daily':
                    df['date'] = pd.to_datetime(df['date'])
                    df.set_index('date', inplace=True)
                else:
                    print(frequency + ': wrong frequency range')
                    return None
            else:
                print('dataframe empty for ' + 'stocks' + " " + str(identifier))
                return None

            return df

        except ApiException as e:
            print("Exception when calling SecurityApi->get_security_stock_prices: %s\r\n" % e)