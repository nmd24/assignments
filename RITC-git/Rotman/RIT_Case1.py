"""
The following parameters will be useful:
ticker      = (STR) Tickers representing securities. In Algorithmic Trading case, we have: "USD", "BULL", "BEAR", "RITC"
type        = (STR) "MARKET" or "LIMIT"
quantity    = (INT) Quantity to trade
action      = (STR) "BUY" or "SELL"
price       = (INT) required for LIMIT orders  -- This is an optional parameter
"""

import requests
from Blackscholes import bsm_call_imp_vol, bsm_put_imp_vol, bsm_vega, bsm_call_delta, bsm_put_delta,implied_volc,implied_volp

# Step 2: Save the API key for easy access:
API_KEY = {"X-API-key": "IB5GYDSA"}


def main():
    # Step 3: Create a Session object to manage connections and requests to the RIT client:
    with requests.Session() as s:
        # Step 4: Add the API key to the Session object to authenticate with every request:
        s.headers.update(API_KEY)
        # mkt_buy_params = {"ticker"  : "RTM"}
        # Step 5: Make a request to the using post() to fulfill the above order:
        resp = s.get("http://localhost:9999/v1/securities")
        resp_ticks = s.get("http://localhost:9999/v1/case")

        # Step 6: Check if the response is as expected:
        if resp.ok and resp_ticks.ok:
            # Step 7: Parse the returned data by calling the json() method:
            mkt_order1 = resp.json()
            mkt_order_ticks = resp_ticks.json()
            # Step 8: Work with the parsed data:
            # id = mkt_order['ticker'] # extract the order id from the object "mkt_order"
            # print(f"Last: {mkt_order1}, Type: {type(mkt_order1)}")
            res_list = []
            v0 = mkt_order1[0]['last']

            # Calculating Time to maturity of the options

            for items in mkt_order1[1:]:
                strike = items['ticker'][-2:]
                total_time = items['ticker'][3]

                if mkt_order_ticks['period'] == 1:
                    TTM_val = 300 * int(total_time) - int(mkt_order_ticks['tick'])
                if mkt_order_ticks['period'] == 2 and total_time == '2':
                    TTM_val = 150 * int(total_time) - int(mkt_order_ticks['tick'])
                if mkt_order_ticks['period'] == 2 and total_time == '1':
                    TTM_val = 0.00000000001
                TTM_val = TTM_val / 3600
                # Creating a list of required parameters

                dict = {'ticker': items['ticker'], 'V0': v0, 'last': items['last'], 'strike': strike, 'TTM': TTM_val}
                res_list.append(dict)
            # print(res_list)

            # Implied Vol Calculation
            for item in res_list:
                if item['ticker'][4] == 'C':
                    imp_vol = implied_volc(
                        price=float(item['last']),
                        s0=item['V0'],
                        K=int(item['strike']),
                        T=float(item['TTM']),
                        r=0.0)
                    delta = bsm_call_delta(S0=item['V0'],
                                           K=int(item['strike']),
                                           r=0.0,
                                           T=float(item['TTM']),
                                           sigma=.2)
                    item['delta'] = delta

                    item['imp_vol'] = imp_vol
                if item['ticker'][4] == 'P':
                    imp_vol = implied_volp(
                        price=float(item['last']),
                        s0=item['V0'],
                        K=int(item['strike']),
                        T=float(item['TTM']),
                        r=0.0)
                    item['imp_vol'] = imp_vol
                    delta = bsm_put_delta(S0=item['V0'],
                                          K=int(item['strike']),
                                          r=0.0,
                                          T=float(item['TTM']),
                                          sigma=.2)
                    item['delta'] = delta

                # vega = bsm_vega(S0=item['V0'], K=int(item['strike']), r=0.0, T=float(item['TTM']), sigma=.2)
                # item['vega']=vega
            # Printing entire portfolio
            print(res_list)














if __name__=="__main__":
    main()
