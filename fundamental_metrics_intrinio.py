import intrinio_sdk
from utils.tickers import Tickers
from utils.metricscalculator import MetricsCalculator
from utils.persister import Persister
import os

#https://data.intrinio.com/data-tags/calculations-metrics


INTRINIO_API = os.getenv('INTRINIO_API')
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = INTRINIO_API


def main():
    metrics = ['ebit', 'freecashflow']

    path = 'json'
    my_value_json = Persister()

    tickers = Tickers()
    fundamentals = MetricsCalculator()

    for ticker in tickers.get_us_tickers():
        for metric in metrics:
            metric_dict = fundamentals.get_company_valuation_metric(ticker, metric)
            my_value_json.to_json(path, ticker, metric_dict, metric)


if __name__ == '__main__':
    main()
