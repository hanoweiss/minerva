import json
from urllib.request import Request, urlopen
from utils_functions import *

def get_revenue_data(comp_ticker, period, num_of_per):
    raw_data = []
    ticker = comp_ticker
    stock_data = get_data_from_api(ticker)

    financial_report = stock_data['financials']['annuals']['income_statement']
    for i in range(5):
        revenue = financial_report["Revenue"][-(i+2)]
        raw_data.append(revenue)
    return raw_data


get_revenue_data("AAPL", 'annuals', 3)
#print('Debt to equity:', debt_to_equity)
#print('Current Ratio:', current_ratio)
#print('Quick Ration:', quick_ratio)
#print('Interest Coverage:', interest_coverage)
