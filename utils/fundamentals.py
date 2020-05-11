import intrinio_sdk
from intrinio_sdk.rest import ApiException


class Fundamentals:

    @staticmethod
    def get_company_metric(ticker, metric):
        identifier = ticker  # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
        tag = metric  # str | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]
        frequency = 'quarterly'  # str | Return historical data in the given frequency (optional) (default to daily)
        type = ''  # str | Return historical data for given fiscal period type (optional)
        start_date = '2010-01-01'  # date | Return historical data on or after this date (optional)
        end_date = ''  # date | Return historical data on or before this date (optional)
        sort_order = 'desc'  # str | Sort by date `asc` or `desc` (optional) (default to desc)
        page_size = 100  # int | The number of results to return (optional) (default to 100)
        next_page = ''  # str | Gets the next page of data from a previous API call (optional)

        try:
            company_api = intrinio_sdk.CompanyApi()
            api_response = company_api.get_company_historical_data(identifier, tag, frequency=frequency, type=type,
                                                                   start_date=start_date, end_date=end_date,
                                                                   sort_order=sort_order, page_size=page_size,
                                                                   next_page=next_page)

            metric_list = list()
            for metric_date_value in api_response.historical_data:
                date_value_dict = {"date": str(metric_date_value.date), "value": str(metric_date_value.value)}
                metric_list.append(date_value_dict)

            metric_dict = dict()
            metric_dict[metric] = metric_list

            return metric_dict

        except ApiException as e:
            print("Exception when calling CompanyApi->get_company_historical_data: %s\r\n" % e)
