import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

API_KEY = {"X-API-key": "IB5GYDSA"}

def main(order_id):
    with requests.Session() as s:
        s.headers.update(API_KEY)
        # order_id = 2365
        resp = s.delete(f"http://localhost:9999/v1/orders/{order_id}")
        if resp.ok:
            status = resp.json()
            success = status["success"]
            print(f"The order was successfully cancelled with code {success}")
        else:
            print("The order could not be cancelled!")

if __name__=="__main__":
    main()
