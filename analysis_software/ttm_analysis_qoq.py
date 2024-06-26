import json
from urllib.request import Request, urlopen
from utils_functions import *



def get_ttm_analysis(comp_ticker):
    ticker = comp_ticker
    stock_data = get_data_from_api(ticker)
    quarterly_data = stock_data['financials']['quarterly']

    #revenue_analysis
    income_statement = quarterly_data['income_statement']
    revenue_data = income_statement['Revenue']
    revenue_last_four_q_data = revenue_data[-5:]
    rev_data = create_ttm_quarters_analysis_dict(revenue_last_four_q_data)

    #print(rev_dict)

    #operating margin
    operating_margin = income_statement['Operating Margin %']
    op_margin_last_four_q_data = operating_margin[-5:]
    op_data = create_ttm_quarters_analysis_dict(op_margin_last_four_q_data)
    #print('Operating margins:', op_margin_last_four_q_data)


    #net income
    net_income_data = income_statement['Net Income']
    net_income_last_four_q_data = net_income_data[-5:]
    net_data = create_ttm_quarters_analysis_dict(net_income_last_four_q_data)
    #print(net_dict)

    #cash from operation
    cash_flow_statement = quarterly_data['cashflow_statement']
    cash_from_operation = cash_flow_statement['Cash Flow from Operations']
    cash_last_four_q_data = cash_from_operation[-5:]
    cash_from_op_data = create_ttm_quarters_analysis_dict(cash_last_four_q_data)
    #print(cash_from_op_dict)

    #free_cash_flow
    cash_flow = cash_flow_statement['Free Cash Flow']
    cash_flow_last_four_q_data = cash_flow[-5:]
    cash_flow_data = create_ttm_quarters_analysis_dict(cash_flow_last_four_q_data)
    #print(cash_flow_dict)

    raw_data = {
        'Revenue': rev_data,
        'Operating margin': op_data,
        'Net income': net_data,
        'Cash from operation': cash_from_op_data,
        'Free cash flow': cash_flow_data
    }


    df = pd.DataFrame(raw_data,
                  index=pd.Index(['YOY change', 'Q1 to Q2 change', 'Q2 to Q3 change', 'Q3 to Q4 change'], name=ticker),
                  columns=pd.Index(['Revenue', 'Operating margin', 'Net income', 'Cash from operation', 'Free cash flow']))

    return df

