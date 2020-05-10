class Companies:

    _us_tickers = ['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'GE', 'GS', 'HD', 'IBM', 'INTC',
               'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UNH', 'UTX',
               'V', 'VZ', 'WMT', 'XOM']

    _es_tickers = ['REE', 'TEF', 'BBVA', 'AMS', 'IBE', 'REP', 'ITX', 'SAN', 'CABK', 'SAB']

    def get_us_tickers(self):
        return self._us_tickers

    def get_es_tickers(self):
        return self._es_tickers
