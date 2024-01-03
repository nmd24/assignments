import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import requests

API_KEY = {"X-API-key" : "ZXZH6DVX"}

def ticker_bid_ask(session, ticker):
    payload = {"ticker":ticker}
    resp = session.get("http://localhost:9999/v1/securities/book", params=payload)
    if resp.ok:
        book = resp.json()
        print(f"The information was successfully fetched!\n")
        bid = book["bids"][0]["price"]
        ask = book["asks"][0]["price"]
        return bid, ask
    else:
        print("The information was not successfully fetched!")

def main():
    # Step 3: Create a Session object to manage connections and requests to the RIT client:
    with requests.Session() as s:
        s.headers.update(API_KEY)
        bid, ask = ticker_bid_ask(s, "BULL")
        print(f"Bid: {bid}, Ask: {ask}")

if __name__=="__main__":
    main()
