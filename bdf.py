import requests
import json
import pandas as pd
import datetime as dt

def get_binance_data(symbol, interval, startTime, endTime):
    url = 'https://api.binance.com/api/v3/klines'  # Fixed URL
    startTime = str(int(startTime.timestamp() * 1000))
    endTime = str(int(endTime.timestamp() * 1000))

    req_params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": startTime,
        "endTime": endTime,
        "limit": 1000
    }

    response = requests.get(url, params=req_params)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.text}")
        return None

    df = pd.DataFrame(json.loads(response.text))  # Fixed typo
    if df.empty:
        return None
    
    df = df.iloc[:, 0:6]
    df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']
    df = df.astype({"open": "float", "high": "float", "low": "float", "close": "float", "volume": "float"})

    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.datetime]

    return df

df_list = []
last_datetime = dt.datetime(2025, 1, 1)
while True:
    print(last_datetime)
    new_df = get_binance_data('SOLUSDT', '5m', last_datetime, dt.datetime.now()) #Name of the crypt and time fram 
    if new_df is None:
        break
    df_list.append(new_df)
    last_datetime = max(new_df.index) + dt.timedelta(seconds=1)  # Fixed typo

df = pd.concat(df_list)
df = df.drop(columns=['datetime'])
df.columns = ["Open", "High", "Low", "Close", "Volume"]  # Fixed spelling

print(df)
df.to_csv("SOLUSDT5m.csv", index_label='Date') #Name of the file in which you want to store
