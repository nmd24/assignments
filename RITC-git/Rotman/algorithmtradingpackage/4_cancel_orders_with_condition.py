import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
"""
Parameters of cancel_params:
all  = 0 for SELL Orders and 1 for BUY Orders
query
"""
API_KEY = {"X-API-key": "57P2J5MY"}

def main():
    with requests.Session() as s:
        s.headers.update(API_KEY)
        cancel_params = {"all": 0,
                         "query": "Price > 1.02 AND VOLUME < 0"}
        resp = s.post("http://localhost:9999/v1/commands/cancel", params = cancel_params)
        if resp.ok:
            status = resp.json()
            cancelled = status["cancelled_order_ids"]
            print(f"The following orders were cancelled: {cancelled}")
        else:
            print("Cancellation of the orders was unsuccessful.")