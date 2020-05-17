from __future__ import print_function
from pprint import pprint
import intrinio_sdk
from intrinio_sdk.rest import ApiException

import pandas as pd

pd.set_option('display.float_format', lambda x: '%.4f' % x)


class MetricsCalculator:

    @staticmethod
    def get_company_valuation_metric(ticker, metric, start_date, end_date, frequency='yearly'):
        identifier = ticker  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
        tag = metric  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]
        frequency = frequency  # str | Return historical data in the given frequency (optional) (default to daily)
        type = ''  # str | Return historical data for given fiscal period type (optional)
        start_date = start_date  # date | Return historical data on or after this date (optional)
        end_date = end_date  # date | Return historical data on or before this date (optional)
        sort_order = 'desc'  # str | Sort by date `asc` or `desc` (optional) (default to desc)
        page_size = 100  # int | The number of results to return (optional) (default to 100)
        next_page = ''  # str | Gets the next page of data from a previous API call (optional)

        try:
            company_api = intrinio_sdk.CompanyApi()
            api_response = company_api.get_company_historical_data(identifier, tag, frequency=frequency, type=type,
                                                                   start_date=start_date, end_date=end_date,
                                                                   sort_order=sort_order, page_size=page_size,
                                                                   next_page=next_page)

            #pprint(api_response)
            df = pd.DataFrame(api_response.historical_data_dict)
            df.rename(columns={"value": metric}, inplace=True)
            if frequency == 'yearly':
                df['date'] = df['date'].apply(lambda x: x.year)
            elif frequency == 'quarterly':
                df['date'] = df['date'].apply(lambda x: str(str(x.year) + '-Q' + str(((x.month-1)//3)+1)))

            df.set_index('date', inplace=True)

            metric_list = list()
            for metric_date_value in api_response.historical_data:
                date_value_dict = {"date": str(metric_date_value.date), "value": str(metric_date_value.value)}
                metric_list.append(date_value_dict)

            return df

            # return metric_list

        except ApiException as e:
            print("Exception when calling CompanyApi->get_company_historical_data: %s\r\n" % e)
