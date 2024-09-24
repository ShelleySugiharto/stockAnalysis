import yfinance as yf
import pandas as pd
import requests as r
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

REQ_RATE = [4,Duration.SECOND * 5] #Constant rate for limiter

#monkey patch the yfinance api for the custom get
original_get = r.get #backup the original get from yf

def custom_get(*args, **kwargs):
    return session.get(*args, **kwargs)

r.get = custom_get #replace with custom get

#user input for period and ticker(s)
print('Choose from 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max')
period = input('Enter desired period:')
tickerList = input('Enter ticker(s) separated by commas, no spaces:')

#make ticker list string into list
if ',' in tickerList:
    tickerList = tickerList.split(',')

else:
    tickerList = [tickerList]

#creates cached sessions to ease amount of yahoo requests
class CachedLimiterSession(CacheMixin, LimiterMixin, r.Session):
    pass

session = CachedLimiterSession(
    limiter = Limiter(RequestRate(REQ_RATE[0], REQ_RATE[1])),
    bucket_class = MemoryQueueBucket,
    backend = SQLiteCache("yfinance.cache")
)

#download data and assign ticker column for all tickers in tickerList
try:
    df = pd.concat([yf.Ticker(ticker).history(period=period).assign(
            ticker=ticker
            ) for ticker in tickerList], 
            ignore_index=True) #removes dates, replaces w ints [0,i]
    
except Exception as e:
    print(f"error dowloading data: {e}")

r.get = original_get #replace the original get to continue w yf

#dictionary with tickers as keys, subcols (eg. 'Open', 'Close', etc.) as vals (list)
d_ticker = {
    ticker: gp.drop(columns='ticker').to_dict(orient='list') for ticker, 
    gp in df.groupby('ticker')
}

print(d_ticker)
