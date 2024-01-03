import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

# Step 1: Import the "requests" package:
import requests

# Step 2: Save the API key for easy access:
API_KEY = {"X-API-key" : "57P2J5MY"}

def main():
    # Step 3: Create a Session object to manage connections and requests to the RIT client:
    with requests.Session() as s:
        # Step 4: Add the API key to the Session object to authenticate with every request:
        s.headers.update(API_KEY)
        # Step 5: Make a request to the appropriate URL endpoint, usually using the get() and post() methods:
        resp = s.get("http://localhost:9999/v1/case")

        # Step 6: Check if the response is as expected:
        if resp.ok:
            # Step 7: Parse the returned data by calling the json() method:
            case = resp.json()
            tick = case['tick'] # accessing the "tick" value that was returned
            # Step 8: Work with the parsed data
            print("The case is on tick", tick)
if __name__=="__main__":
    main()
