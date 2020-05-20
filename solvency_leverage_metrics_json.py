from utils.persistor import Persistor
from utils.tickers import Tickers
from utils.metricnames import MetricNames

def main():


    persistor = Persistor()

    tickers = Tickers()
    metrics = MetricNames()

    for ticker in tickers.get_us_tickers():
        for metric in metrics.get_solvency_leverage_metrics():
            df = persistor.read_pickle('pickle', ticker, metric, 'solvency_leverage')
            persistor.write_json_quarterly_basis('json/', ticker, metric, df, 'solvency_leverage')


if __name__ == '__main__':
    main()