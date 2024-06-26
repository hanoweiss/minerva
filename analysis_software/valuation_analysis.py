# inputs:
# 1. FCF - 7 years average
# 2. Number of shares
# 3. growth rate - FCF grow thrate
# 4. discounted rate - desired return (usually WACC)
# 5. perpetuity growth rate - inflation/ pupolation growth rate - 2%-3%
# 6. number of years - short term
# 7. number of years long terms
# 8. margin of saftey - 50%
from utils_functions import *

ticker = 'csco'
num_of_years = 5  # for average free cash flow
short_term_growth_rate = 0.05
long_term_growth_rate = 0
discount_rate = 0.07  # WACC
short_term_years = 10
long_term_years = 10
perpetuity_growth_rate = 0.02
margin_of_safety = 0.5


stock_data = get_data_from_api(ticker)


def get_avg_free_cash_flow(stock_data, num_of_years):
    cashflow_statement = stock_data['financials']['annuals']['cashflow_statement']
    fcf = cashflow_statement['Free Cash Flow']
    avg_free_cash_flow = calc_avg(fcf, num_of_years)
    return avg_free_cash_flow


free_Cash_flow = get_avg_free_cash_flow(stock_data, num_of_years)


def get_number_of_shares(stock_data):
    nos = stock_data['financials']['annuals']['income_statement']['Shares Outstanding (Diluted Average)'][-1]
    return float(nos)


num_of_shares = get_number_of_shares(stock_data)


def calculate_intrinsic_value(fcf, nos, st_growth, lt_growth, dr, st_years, lt_years, pgr, mos):
    npv_st_fcf = 0
    npv_lt_fcf = 0
    st_lt_delta = lt_years - st_years
    for i in range(1, st_years + 1):
        npv_st_fcf += (fcf * (1 + st_growth) ** i)/((1+dr) ** i)
    for i in range(st_years, lt_years + 1):
        npv_lt_fcf = (fcf * (1 + lt_growth) ** (st_years + i))/((1+dr) ** (st_years + i)) if lt_years != st_years else 0
    pv_fcf = npv_st_fcf + npv_lt_fcf
    pv_perp_fcf = ((fcf * ((1+st_growth) ** (st_years+1)) * ((1 + lt_growth) ** st_lt_delta) * (1 + pgr)) / (dr - pgr))\
                  * (1/((1+dr)**(lt_years + 1)))
    intrinsic_value = pv_fcf + pv_perp_fcf
    intrinsic_value_per_share = intrinsic_value / nos
    mos_value = intrinsic_value_per_share * mos

    return intrinsic_value_per_share, mos_value


intrinsic_value, mos_value = calculate_intrinsic_value(free_Cash_flow, num_of_shares, short_term_growth_rate,
                                                       long_term_growth_rate, discount_rate, short_term_years,
                                                       long_term_years, perpetuity_growth_rate, margin_of_safety)


print('The intrinsic value of:', ticker, 'is', intrinsic_value, 'and the margin of safety value is:', mos_value)
