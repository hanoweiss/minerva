import json
from urllib.request import Request, urlopen
from utils_functions import *

ticker = 'CSCO'
long_period = 7
medium_period = 5
last_year = 3


def get_financial_analysis_numbers(ticker, long_period, medium_period, last_year):
    stock_data = get_data_from_api(ticker)
    common_size_ratios = stock_data['financials']['annuals']['common_size_ratios']
    income_statement = stock_data['financials']['annuals']['income_statement']
    cashflow_statement = stock_data['financials']['annuals']['cashflow_statement']
    per_share_data = stock_data['financials']['annuals']['per_share_data_array']
    roe = common_size_ratios['ROE %']
    roic = common_size_ratios['ROIC %']
    revenue = income_statement['Revenue']
    net_income = income_statement['Net Income']
    bvps = per_share_data['Book Value per Share']
    fcf = cashflow_statement['Free Cash Flow']

    roic_avg = {"ROIC {} years growth average".format(long_period): calc_avg(roic, long_period),
               "ROIC {} years growth average".format(medium_period): calc_avg(roic, medium_period),
               "ROIC {} years growth average".format(last_year): calc_avg(roic, last_year)}

    revenue_growth_rates = {"Revenue {} years growth average".format(long_period): calc_avg_growth_rate(revenue, long_period),
               "Revenue {} years growth average".format(medium_period): calc_avg_growth_rate(revenue, medium_period),
               "Revenue {} years growth average".format(last_year): calc_avg_growth_rate(revenue, last_year)}

    net_income_growth_rates = {"Net income {} years growth average".format(long_period): calc_avg_growth_rate(net_income, long_period),
               "Net income {} years growth average".format(medium_period): calc_avg_growth_rate(net_income, medium_period),
               "Net income {} years growth average".format(last_year): calc_avg_growth_rate(net_income, last_year)}

    bvps_growth_rates = {"Book Value {} years growth average".format(long_period): calc_avg_growth_rate(bvps, long_period),
               "Book value {} years growth average".format(medium_period): calc_avg_growth_rate(bvps, medium_period),
               "Book value {} years growth average".format(last_year): calc_avg_growth_rate(bvps, last_year)}

    fcf_growth_rates = {"Free cash flow {} years growth average".format(long_period): calc_avg_growth_rate(fcf, long_period),
               "Free cash flow {} years growth average".format(medium_period): calc_avg_growth_rate(fcf, medium_period),
               "Free cash flow {} years growth average".format(last_year): calc_avg_growth_rate(fcf, last_year)}

    return [roic_avg, revenue_growth_rates, net_income_growth_rates, bvps_growth_rates, fcf_growth_rates]


financial_dicts = get_financial_analysis_numbers(ticker, long_period, medium_period, last_year)
export_to_excel_financial_analysis(financial_dicts)


