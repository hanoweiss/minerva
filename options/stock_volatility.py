import yfinance as yf
import datetime as dt

ticker = yf.Ticker("TLT")
start = dt.datetime.now() - dt.timedelta(days=360)
start_day_string = start.strftime('%Y-%m-%d')
end = dt.datetime.now()
# timeframe is the time which i want to check the max volatility
time_frame = 21
total_time = 360

close_prices_raw = yf.download(ticker.ticker, start_day_string)['Adj Close']
close_prices_array = close_prices_raw.values


def daily_vol(first_day_close, second_day_close):
    return (second_day_close / first_day_close) - 1
    #add indication of what is the dates with the highest change


def max_vol_in_time_frame(time_frame, close_prices_array):
        max_vol = 0
        for i in range(len(close_prices_array) - 1):
            for j in range(time_frame):
                if i + j > len(close_prices_array) - 1:
                    break
                daily = daily_vol(close_prices_array[i], close_prices_array[i + j])
                if abs(daily) > max_vol:
                    max_vol = abs(daily)
                    first_value = (close_prices_array[i], i)
                    second_value = (close_prices_array[i+j], i+j)
            if j == time_frame:
                break
        return max_vol*100, first_value, second_value

result = max_vol_in_time_frame(time_frame, close_prices_array)
print(result)
print(close_prices_raw.index[result[1][1]], close_prices_raw.index[result[2][1]])


def avg_vol_in_time_frame():
    # calcualte the average volatility in time period for a specific time frame -
    # for example 14 days volatility measured on 1 year
    return 0