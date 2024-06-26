import json
from urllib.request import Request, urlopen
from utils_functions import *


def get_debt_analysis(comp_ticker):
    ticker = comp_ticker
    stock_data = get_data_from_api(ticker)

    common_size_ratios = stock_data['financials']['annuals']['common_size_ratios']
    valuation_and_quality = stock_data['financials']['annuals']['valuation_and_quality']

    debt_to_equity = get_last_year_item(common_size_ratios['Debt-to-Equity'])
    current_ratio = get_last_year_item(valuation_and_quality['Current Ratio'])
    quick_ratio = get_last_year_item(valuation_and_quality['Quick Ratio'])
    interest_coverage = get_last_year_item(valuation_and_quality['Interest Coverage'])

    raw_data = [debt_to_equity, current_ratio, quick_ratio, interest_coverage]
    return raw_data



#print('Debt to equity:', debt_to_equity)
#print('Current Ratio:', current_ratio)
#print('Quick Ration:', quick_ratio)
#print('Interest Coverage:', interest_coverage)
