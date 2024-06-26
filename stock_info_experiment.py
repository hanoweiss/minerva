import yfinance

from datetime import *
import pandas
from pandas import *
from yfinance import *


aso = yfinance.Ticker("ASO")
hist = aso.history(period="max")
print(hist)


today = date.today()
quarter = pandas.Timestamp(date(today.year, today.month, today.day)).quarter

stop = 4


# To develop:
# 1. YTD return
# 2. Quarters returns
# 3. last week returns
# 4. indexes returns
# 5. last month
# 6. last year
# 7. years returns
