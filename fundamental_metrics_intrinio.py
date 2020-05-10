import intrinio_sdk
from utils.tickers import Tickers
from utils.fundamentals import Fundamentals
from utils.my_value_json import MyValueJson

#https://data.intrinio.com/data-tags/calculations-metrics


intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjA5ZGY4MWI2NjM1NDZkMDE5MzAxYzNkZDIxOTg1ZTMz'


def main():
    metrics = ['ebit', 'freecashflow']

    path = 'json'
    my_value_json = MyValueJson()

    tickers = Tickers()
    fundamentals = Fundamentals()

    for ticker in tickers.get_us_tickers():
        for metric in metrics:
            metric_dict = fundamentals.get_company_metric(ticker, metric)
            my_value_json.to_json(path, ticker, metric_dict, metric)


if __name__ == '__main__':
    main()
