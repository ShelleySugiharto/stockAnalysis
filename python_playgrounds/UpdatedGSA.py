import yfinance as yf
import pandas as pd
import requests as r
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

#monkey patch the yfinance api for the custom get

original_get = r.get #backup the original get from yf

def custom_get(*args, **kwargs):
    return session.get(*args, **kwargs)

r.get = custom_get #replace with custom get

#define vars
period = '1d'
tickerList = ["AMZN"]
ReqRate = [4,Duration.SECOND * 5]

#creates cached sessions to ease amount of yahoo requests
class CachedLimiterSession(CacheMixin, LimiterMixin, r.Session):
    pass

session = CachedLimiterSession(
    limiter = Limiter(RequestRate(ReqRate[0], ReqRate[1])),
    bucket_class = MemoryQueueBucket,
    backend = SQLiteCache("yfinance.cache")
)

#download data and assign ticker column for all tickers in tickerList
try:
    df = pd.concat([yf.Ticker(ticker).history(period=period).assign(
            ticker=ticker
            ) for ticker in tickerList], 
            ignore_index=True)
    
except Exception as e:
    print(f"error dowloading data: {e}")

r.get = original_get #replace the original get to continue w yf

print(df.head()) #check df

#parse through df and separate columns
#dictionary for df
#if multiple tickers, receiving data from each subcol would need separation
#if single ticker, index is subcol (eg. 'Close', 'Open', etc.)

d = {idx: gp.T for idx,
     gp in df.T.groupby(level=0) 
     }

