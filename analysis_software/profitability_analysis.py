import json
from utils_functions import *

ticker = 'CSCO'
stock_data = get_data_from_api(ticker)

#gross margin - last year 7 years avg
#operating margin
#net margin
#cash flow from operation
#capex
#capes to operating cash flow
#free cash flow

common_size_ratios = stock_data['financials']['annuals']['common_size_ratios']
gross_margin_avg = calc_avg(common_size_ratios['Gross Margin %'], 8)
print('Gross margin average:', gross_margin_avg, '%')
operating_margin_avg = calc_avg(common_size_ratios['Operating Margin %'], 8)
print('Operating margin average:', operating_margin_avg, '%')
net_margin_avg = calc_avg(common_size_ratios['Net Margin %'], 8)
print('Net margin average:', net_margin_avg, '%')

cash_flow_statement = stock_data['financials']['annuals']['cashflow_statement']
cash_flow_from_operation = calc_avg(cash_flow_statement['Cash Flow from Operations'], 8)
print('Cash flow from operations:', cash_flow_from_operation, '$')
capex = - calc_avg(cash_flow_statement['Capital Expenditure'], 8)
print('Capital Expenditure:', capex, '$')
capex_to_operating_income = calc_avg(common_size_ratios['Capex-to-Operating-Income'], 8)
print('Capex to operating income:', capex_to_operating_income, '%')

free_cash_flow = calc_avg(cash_flow_statement['Free Cash Flow'], 8)
print('Free Cash Flow:', free_cash_flow, '$')
