# Historical-crypto-candle-data
# Binance Crypto Candle Data Fetcher (No API Key Required)
# Overview

This Python script fetches historical candlestick (OHLCV) data for any cryptocurrency listed on Binance without requiring an API key. It retrieves data within a specified time range and saves it as a CSV file for further analysis.

# Features

Fetch candle (OHLCV) data from Binance without an API key.

Supports any trading pair listed on Binance.

Supports multiple timeframes (e.g., 1m, 5m, 1h, 1d, etc.).

Retrieves data in chunks and appends it for seamless time-series analysis.

Saves data in a structured CSV format for easy use.

# Installation
 Prerequisites
  Ensure you have Python 3.x installed along with the required dependencies.
    # Install Required Libraries
    1) pip install requests pandas
  # Usage
  1. Run the Script
     Save the script as fetch_binance_data.py and execute it:
    => python fetch_binance_data.py
  2. Modify Trading Pair & Timeframe
      You can change the following parameters inside the script:
      symbol = 'SOLUSDT'  # Change to your desired trading pair
      interval = '5m'      # Change to desired timeframe (e.g., '1m', '1h', '1d')
   3. Modify Start & End Time
      The script fetches data from a given start time to the current time. You can modify:
      last_datetime = dt.datetime(2025, 1, 1)  # Change the start date
   4. Save Data as CSV
      The script automatically saves data in a CSV file: SOLUSDT5m.csv
      If needed, change the filename in:
      df.to_csv("SOLUSDT5m.csv", index_label='Date')

      
Example Output

                   Open     High      Low    Close   Volume
2025-01-01 00:05  123.45  125.00  122.30  124.50  1000.23
2025-01-01 00:10  124.50  126.10  123.90  125.75   950.67
...

# Code Explanation

Function: get_binance_data()

Fetches OHLCV data from Binance API.

Converts timestamps to readable datetime format.

Structures data into a Pandas DataFrame.

While Loop

Iteratively fetches data in chunks from start_time to end_time.

Appends the retrieved data to a list and concatenates it.

Timeframe Options

Interval

Meaning

1m = 1 Minute
5m = 5 Minutes
15m = 15 Minutes
1h = 1 Hour
4h = 4 Hours
1d = 1 Day
1w = 1 Week

Notes

This script uses Binance's public REST API.

Binance allows a maximum of 1000 candles per request.

If data fetching is slow, try increasing the time range in chunks.

If Binance blocks requests, consider adding a short delay between API calls.

License

This project is open-source under the MIT License.

Contributions

Feel free to contribute by improving error handling, adding features, or optimizing performance!

Contact

For any issues or improvements, open an issue on GitHub!

🚀 Happy Trading! 🎯

Follow me one social media 
Same i'd on every plateform:-
# @ayushk2s
