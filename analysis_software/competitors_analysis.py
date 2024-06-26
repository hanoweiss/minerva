import json
from urllib.request import Request, urlopen
from utils_functions import *
from debt_analysis import get_debt_analysis
from ttm_analysis_qoq import get_ttm_analysis

tickers = ['lpx', 'wfg']
comparison_table = {}
data_frames = []
def debt_comparison(tickers, comparison_table):
    for ticker in tickers:
        raw_data = get_debt_analysis(ticker)
        comparison_table[ticker] = raw_data


    df = pd.DataFrame(comparison_table,
                      index=pd.Index(['Debt to equity', 'Current ratio', 'Quick ration', 'Interest coverage']),
                      columns=pd.Index(tickers))
    return df

def ttm_analysis_comparison(tickers):
    dfs = []
    for ticker in tickers:
        df = get_ttm_analysis(ticker)
        dfs.append(df)
    return dfs


debt_comparison = debt_comparison(tickers, comparison_table)
data_frames.append(debt_comparison)
ttm_analysis_dfs = ttm_analysis_comparison(tickers)


data_frames_to_export = data_frames + ttm_analysis_dfs
print(data_frames_to_export)
export_to_excel(data_frames_to_export, 'output.xlsx')


#ToDo: add profitability comparison