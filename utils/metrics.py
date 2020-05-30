from __future__ import print_function
from pprint import pprint
import intrinio_sdk
from intrinio_sdk.rest import ApiException

from datequarter import DateQuarter

import pandas as pd

pd.set_option('display.float_format', lambda x: '%.4f' % x)


class Metrics:

    @staticmethod
    def get_company_metrics(ticker, metric, start_date, end_date, frequency='yearly', next_page=''):
        identifier = ticker  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
        tag = metric  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]
        frequency = frequency  # str | Return historical data in the given frequency (optional) (default to daily)
        type = ''  # str | Return historical data for given fiscal period type (optional)
        start_date = start_date  # date | Return historical data on or after this date (optional)
        end_date = end_date  # date | Return historical data on or before this date (optional)
        sort_order = 'desc'  # str | Sort by date `asc` or `desc` (optional) (default to desc)
        page_size = 100  # int | The number of results to return (optional) (default to 100)
        next_page = next_page  # str | Gets the next page of data from a previous API call (optional)

        try:
            company_api = intrinio_sdk.CompanyApi()
            api_response = company_api.get_company_historical_data(identifier, tag, frequency=frequency, type=type,
                                                                   start_date=start_date, end_date=end_date,
                                                                   sort_order=sort_order, page_size=page_size,
                                                                   next_page=next_page)

            #pprint(api_response)
            df = pd.DataFrame(api_response.historical_data_dict)
            if not df.empty:
                df.rename(columns={"value": metric}, inplace=True)
                if frequency == 'yearly':
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
                print('dataframe empty for ' + str(metric) + " " + str(identifier))
                return None

            return df

        except ApiException as e:
            print("Exception when calling CompanyApi->get_company_historical_data: %s\r\n" % e)
