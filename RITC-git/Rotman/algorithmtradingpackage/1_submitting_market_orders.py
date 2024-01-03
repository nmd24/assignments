import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
"""
The following parameters will be useful:
ticker      = (STR) Tickers representing securities. In Algorithmic Trading case, we have: "USD", "BULL", "BEAR", "RITC"
type        = (STR) "MARKET" or "LIMIT"
quantity    = (INT) Quantity to trade
action      = (STR) "BUY" or "SELL"
price       = (INT) required for LIMIT orders  -- This is an optional parameter
"""
# Step 1: Import the "requests" package:
import requests

# Step 2: Save the API key for easy access:
API_KEY = {"X-API-key" : "ZXZH6DVX"}

def main():
    # Step 3: Create a Session object to manage connections and requests to the RIT client:
    with requests.Session() as s:
        # Step 4: Add the API key to the Session object to authenticate with every request:
        s.headers.update(API_KEY)
        mkt_buy_params = {"ticker"  : "RITC",
                          "type"    : "MARKET",
                          "quantity": 1000,
                          "action"  : "BUY"}
        # Step 5: Make a request to the using post() to fulfill the above order:
        resp = s.post("http://localhost:9999/v1/orders", params = mkt_buy_params)
        # Step 6: Check if the response is as expected:
        if resp.ok:
            # Step 7: Parse the returned data by calling the json() method:
            mkt_order = resp.json()
            status = resp2.json()
            print(status[4])
            for stock in status:
                if stock['ticker'] == 'RITC' and stock['position'] > 0:
                    print("yes")
            print("no")

if __name__=="__main__":
    main()
