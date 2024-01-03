import pandas as pd
import numpy as np
import requests

API_KEY = {"X-API-key" : "ZXZH6DVX"}

"""
The following parameters will be useful:
ticker      = (STR) Tickers representing securities. In Algorithmic Trading case, we have: "USD", "BULL", "BEAR", "RITC"
type        = (STR) "MARKET" or "LIMIT"
quantity    = (INT) Quantity to trade
action      = (STR) "BUY" or "SELL"
price       = (INT) required for LIMIT orders  -- This is an optional parameter
"""

def main():
    with requests.Session() as s:
        s.headers.update(API_KEY)
        lmt_sell_params = {"ticker"   : "USD",
                           "type"     : "LIMIT",
                           "quantity" : 100,
                           "action"   : "BUY",
                           "price"    : 1.04}
        resp = s.post("http://localhost:9999/v1/orders", params = lmt_sell_params)
        param_order = {
            "order_id" : 164,
            "ticker":"USD"
        }
        resp2 = s.get("http://localhost:9999/v1/orders", params="OPEN")
        if resp.ok:
            lmt_order = resp.json()
            id = lmt_order["order_id"]
            status = resp2.json()

            print(f"The limit sell order was submitted successfully with ID: {id}")
            print(f"The order is open = {status}")
        else:
            print("The order was not successfully submitted!")
if __name__=="__main__":
    main()
