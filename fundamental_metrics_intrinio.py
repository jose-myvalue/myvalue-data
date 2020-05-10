import intrinio_sdk
from utils.companies import Companies
from metrics.fundamentals import Fundamentals
from utils.my_value_json import MyValueJson
import json

#https://data.intrinio.com/data-tags/calculations-metrics


intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'


def main():
    metrics = ['ebit', 'freecashflow']

    path = 'json'
    my_value_json = MyValueJson()

    companies = Companies()
    tickers = companies.get_us_tickers()
    fundamentals = Fundamentals()

    for ticker in tickers:
        for metric in metrics:
            metric_dict = fundamentals.get_company_metric(ticker, metric)
            my_value_json.to_json(path, ticker, metric_dict, metric)


if __name__ == '__main__':
    main()
