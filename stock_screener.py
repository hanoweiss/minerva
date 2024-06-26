import pandas_datareader as web
import pandas as pd
from yahoo_fin import stock_info as si
import datetime as dt

tickers = si.tickers_sp500()
start = dt.datetime.now() - dt.timedelta(days=365)
end = dt.datetime.now()

sp500_df = web.DataReader('^GSPC', 'yahoo', start, end)
sp500_df['pct change'] = sp500_df['adj closer'].pct_change()
sp500_return = (sp500_df['pct change' + 1]).cumprod()[-1]

returns_list = []
final_df = pd.DataFrame(columns=['ticker', 'latest price', 'pe ration', '52 week low', '52 week high'])


for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', start, end)
    df.to_csv(f'stock_data/{ticker}.csv')
    df['pct change'] = df['adj closer']
    stock_return = (df['pct change' + 1]).cumprod()[-1]
    returns_compared = round((stock_return/sp500_return), 2)
    returns_list.append(returns_compared)

best_performers = pd.DataFrame(list(zip(tickers, returns_list)), columns=['tickers', 'returns compared'])


