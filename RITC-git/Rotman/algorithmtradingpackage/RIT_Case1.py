"""
The following parameters will be useful:
ticker      = (STR) Tickers representing securities. In Algorithmic Trading case, we have: "USD", "BULL", "BEAR", "RITC"
type        = (STR) "MARKET" or "LIMIT"
quantity    = (INT) Quantity to trade
action      = (STR) "BUY" or "SELL"
price       = (INT) required for LIMIT orders  -- This is an optional parameter
"""
import cancelling_order
import requests
from Blackscholes import bsm_call_imp_vol, bsm_put_imp_vol, bsm_vega, bsm_call_delta, bsm_put_delta,implied_volc,implied_volp,buy_market,sell_market
import matplotlib.pyplot as plt
import numpy as np
# Step 2: Save the API key for easy access:
API_KEY = {"X-API-key": "IB5GYDSA"}
# import pdb
# pdb.set_trace()
def prereq():
    with requests.Session() as s:
        s.headers.update(API_KEY)
        # mkt_buy_params = {"ticker"  : "RTM"}
        # Step 5: Make a request to the using post() to fulfill the above order:
        #resp = s.get("http://localhost:9999/v1/securities")
        #resp_ticks = s.get("http://localhost:9999/v1/case")
        resp = s.post("http://localhost:9999/v1/commands/cancel?all=1")

def main(cancel_list):
    # Step 3: Create a Session object to manage connections and requests to the RIT client:
    #prereq()
    with requests.Session() as s:
        # Step 4: Add the API key to the Session object to authenticate with every request:
        s.headers.update(API_KEY)
        # mkt_buy_params = {"ticker"  : "RTM"}
        # Step 5: Make a request to the using post() to fulfill the above order:
        #resp = s.get('http://localhost:9999/v1/orders?status=TRANSACTED')
        #resp = s.post("http://localhost:9999/v1/commands/cancel?all=1")
        resp = s.get("http://localhost:9999/v1/securities")
        resp_ticks = s.get("http://localhost:9999/v1/case")
        #resp = s.post("http://localhost:9999/v1/commands/cancel?all=1")
        # Step 6: Check if the response is as expected:
        if resp.ok and resp_ticks.ok:
            #http://localhost:9999/v1/commands/cancel?all=1

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
            #print(res_list)

            strikes = []
            imp_volatilities = []
            for i in range(len(res_list)):
                strikes.append(res_list[i]["strike"])
                imp_volatilities.append(res_list[i]["imp_vol"])
            plt.scatter(strikes, imp_volatilities)
            plt.axhline(y=0.20, color='r', linestyle='-')
            plt.axhline(y=0.250, color='b', linestyle='--')
            plt.grid()
           #plt.show()
            realized_volatility = 0.250
            #dict_above = {res_list[i]["ticker"]: res_list[i]["imp_vol"] for i in range(40) if res_list[i]["imp_vol"] >= realized_volatility}

            #dict_below = {res_list[i]["ticker"]: res_list[i]["imp_vol"] for i in range(40) if res_list[i]["imp_vol"] < realized_volatility}
            #max_above = max(dict_above, key=dict_above.get)
            #max_below = max(dict_below, key=dict_below.get)
            dict_below_tolerance = {}
            dict_above_tolerance = {}
            cancel_list_temp = []
            delta_cum = 0
            for i in range(40):
                # delta_cum = 0
                if res_list[i]["imp_vol"] == None:
                    continue
                if res_list[i]["imp_vol"] == 0.01:
                    continue
                elif res_list[i]["imp_vol"] < 0.20 and res_list[i]["last"]>0.5 and int(res_list[i]["strike"])<50 and res_list[i]["ticker"][4]=="C":
                    dict_below_tolerance[res_list[i]["ticker"]]=res_list[i]["imp_vol"]
                    delta_cum+=delta_calc(res_list[i])


                elif res_list[i]["imp_vol"] > 0.20 and res_list[i]["last"]>0.5 and int(res_list[i]["strike"])>50 and res_list[i]["ticker"][4]=="P":
                    dict_above_tolerance[res_list[i]["ticker"]]=res_list[i]["imp_vol"]
                    delta_cum += delta_calc(res_list[i])
                else:
                    continue
            order_size=30
            delta_cum=(delta_cum)*100*order_size
            #print(delta_cum)


            # dict_above_tolerance = {res_list[i]["ticker"]: res_list[i]["imp_vol"] for i in range(40) if res_list[i]["imp_vol"] == None: continue else:res_list[i]["imp_vol"] < 0.20}
            #print(dict_above_tolerance)
            #print(dict_below_tolerance)
            # print(cancel_list)


            for key in dict_below_tolerance.keys():
                return_id = buy_market(s,key,30)
                if return_id != 0: cancel_list_temp.append(return_id)

            for key in dict_above_tolerance.keys():
                return_id = sell_market(s,key,30)
                if return_id != 0: cancel_list_temp.append(return_id)
            print(delta_cum)
            if delta_cum < 0:
                return_id= buy_market(s, 'RTM', int(delta_cum))
                if return_id != 0: cancel_list_temp.append(return_id)
            else:
                return_id= sell_market(s, 'RTM', int(delta_cum))
                if return_id != 0: cancel_list_temp.append(return_id)
            print(cancel_list)

    return cancel_list_temp


            #print(res_list)

def delta_calc(param):
    return(param["delta"])















if __name__=="__main__":
    main()
