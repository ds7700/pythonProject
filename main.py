import requests
import json
import pandas as pd
import datetime
print ("cto nyjno?")
symb = input()
def candles(symb,tf):
    url = 'https://fapi.binance.com/fapi/v1/klines'
    param = {'symbol': symb, 'interval': '1m'}
    r = requests.get(url, params=param)
    if r.status_code == 200:
       df = pd.DataFrame(r.json())
       m = pd.DataFrame()
       m['date'] = df.iloc[:,0]
       m['date'] = pd.to_datetime(m['date'], unit = 'ms')
       m['open'] = df.iloc[:,1].astype(float)
       m['high'] = df.iloc[:, 2].astype(float)
       m['low'] = df.iloc[:, 3].astype(float)
       m['close'] = df.iloc[:, 4].astype(float)
       return m
    else:
        return print("error")

k = candles(symb,'1m')
print(k)