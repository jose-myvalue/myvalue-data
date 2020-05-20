class MetricNames:

#['ebit', 'ebitda', 'freecashflow', 'altmanzscore', 'currentratio', 'debttoequity','ebittointerestex',
# 'marketcap','debttoebitda', 'profitmargin', 'enterprisevalue', 'volume']

#currentratio: non daily data

    #daily basis
    _valuation_metrics = ['evtoebit', 'evtoebitda', 'enterprisevalue', 'pricetoearnings', 'dividendyield',
                          'marketcap', 'pricetobook']

    #quarterly basis
    _solvency_leverage_metrics = ['debttoequity', 'netdebt', 'leverageratio', 'debttoebitda', 'altmanzscore']

    #quarterly basis (percentages)
    _efectiveness_metrics = ['roe', 'roa', 'roce']

    #quarterly basis
    _liquidity_metrics = ['currentratio']

    #quarterly basis
    _profitability_metrics = ['grossmargin']



    def get_valuation_metrics_names(self):
        return self._valuation_metrics

    def get_solvency_leverage_metrics(self):
        return self._solvency_leverage_metrics
