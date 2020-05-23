from persistor import Persistor
from utils.tickers import Tickers
from utils.metricnames import MetricNames

def main():


    persistor = Persistor()

    tickers = Tickers()
    metrics = MetricNames()

    for ticker in tickers.get_us_tickers():
        for metric in metrics.get_efectiveness_metrics():
            df = persistor.read_pickle('pickle', ticker, metric, 'efectiveness')
            if df is not None:
                persistor.write_dataframe_to_json_quarterly_basis('json/', ticker, metric, df, 'efectiveness')
            else:
                print(ticker + ' '  + metric + ' ' + 'dataframe doesn\'t exits')


if __name__ == '__main__':
    main()