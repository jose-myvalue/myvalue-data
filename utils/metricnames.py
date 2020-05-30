class MetricNames:

#, 'ebittointerestex',

    #daily basis
    _valuation_metrics = ['evtoebit', 'evtoebitda', 'enterprisevalue', 'pricetoearnings', 'dividendyield',
                          'marketcap', 'pricetobook', 'earningsyield', 'marketcap']

    #quarterly basis
    _solvency_leverage_metrics = ['debttoequity', 'netdebt', 'leverageratio', 'debttoebitda', 'altmanzscore',
                                  'bookvaluepershare', 'cashdividendspershare', 'totalrevenue', 'ebitda', 'ebit',
                                  'totalassets','freecashflow', 'depreciationandamortization', 'nwc', 'ebitmargin',
                                  'revenuegrowth', 'nwctorev']

    #quarterly basis (percentages)
    _efectiveness_metrics = ['roe', 'roa', 'roce', 'totalequity']

    #quarterly basis
    _liquidity_metrics = ['currentratio']

    #quarterly basis
    _profitability_metrics = ['grossmargin', 'netincome', 'capex', 'ebitdamargin', 'ebitmargin', 'profitmargin']

    #quarterly basis
    _growth_metrics = ['epsgrowth']

    _industry_comparation_metrics = ['pricetobook', 'pricetoearnings', 'roe', 'roa', 'roce']



    def get_valuation_metrics_names(self):
        return self._valuation_metrics

    def get_solvency_leverage_metrics(self):
        return self._solvency_leverage_metrics

    def get_efectiveness_metrics(self):
        return self._efectiveness_metrics

    def get_liquidity_metrics(self):
        return self._liquidity_metrics

    def get_profitability_metrics(self):
        return self._profitability_metrics

    def get_industry_comparation_metrics(self):
        return self._industry_comparation_metrics