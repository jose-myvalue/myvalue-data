from persistor import Persistor
from utils.tickers import Tickers
from utils.metricnames import MetricNames


def main():


    persistor = Persistor()

    tickers = Tickers()
    metrics = MetricNames()

    for ticker in tickers.get_us_tickers():
        for metric in metrics.get_valuation_metrics_names():
            df = persistor.read_pickle('pickle', ticker, metric, 'valuation')
            persistor.write_dataframe_to_json_daily_basis('json/', ticker, metric, df, 'valuation')


if __name__ == '__main__':
    main()
