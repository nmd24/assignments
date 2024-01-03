def bsm_call_value(S0, K, r, T, sigma):

    from math import log, sqrt, exp
    import numpy as np
    from scipy import stats
    
    S0 = float(S0)
    d1 = ( np.log(S0/K) + (r + sigma**2/2.)*T ) / (sigma*np.sqrt(T))
    d2 = ( np.log(S0/K) + (r - sigma**2/2.)*T ) / (sigma*np.sqrt(T))
    option_pv = (S0*stats.norm.cdf(d1, 0.0, 1.0)) - (K*np.exp(-r*T)*stats.norm.cdf(d2, 0.0, 1.0))
    
    return option_pv
#Calculatint Vega of Options
def bsm_vega(S0, K, r, T, sigma):

    from math import log, sqrt, exp
    import numpy as np
    from scipy import stats
    
    S0 = float(S0)
    d1 = ( np.log(S0/K) + (r + sigma**2/2.)*T ) / (sigma*np.sqrt(T))
    vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * np.sqrt(T)
    
    return vega

#Call Implied Vol Cal
def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est):

    sigma_est -= ((bsm_call_value(S0, K, r, T, sigma_est)-C0)
                    / bsm_vega(S0, K, r, T, sigma_est))
    return sigma_est


def bsm_put_value(S0, K, r, T, sigma):
    from math import log, sqrt, exp
    import numpy as np
    from scipy import stats

    S0 = float(S0)
    d1 = (np.log(S0 / K) + (r + sigma ** 2 / 2.) * T) / (sigma * np.sqrt(T))

    d2 = (np.log(S0 / K) + (r - sigma ** 2 / 2.) * T) / (sigma * np.sqrt(T))
    option_pv = (K * np.exp(-r * T) * stats.norm.cdf(-d2, 0.0, 1.0))-(S0 * stats.norm.cdf(-d1, 0.0, 1.0))

    return option_pv

#Put Implied Vol Cal
def bsm_put_imp_vol(S0, K, T, r, C0, sigma_est):
    sigma_est -= ((bsm_put_value(S0, K, r, T, sigma_est) - C0)
                  / bsm_vega(S0, K, r, T, sigma_est))
    return sigma_est
#Call Delta Cal
def bsm_call_delta(S0, K, r, T, sigma):
    import numpy as np
    from scipy import stats

    S0 = float(S0)
    d1 = (np.log(S0 / K) + (r + sigma ** 2 / 2.) * T) / (sigma * np.sqrt(T))
    delta =stats.norm.cdf(d1, 0.0, 1.0)
    return delta

# Put Delta Cal
def bsm_put_delta(S0, K, r, T, sigma):
    import numpy as np
    from scipy import stats

    S0 = float(S0)
    d1 =- -((np.log(S0 / K) + (r + sigma ** 2 / 2.) * T) )/ (sigma * np.sqrt(T))
    delta =-stats.norm.cdf(-d1, 0.0, 1.0)
    return delta

def implied_volc(price,s0,K,T,r):
    import numpy as np
    from scipy import stats
    sigma=0.01
    rtm_sgima=0.2
    while sigma<1:
        S0 = float(s0)
        d1 = (np.log(S0 / K) + (r + sigma ** 2 / 2.) * T) / (sigma * np.sqrt(T))
        d2=( np.log(S0/K) + (r - sigma**2/2.)*T ) / (sigma*np.sqrt(T))
        price_implied=S0*stats.norm.cdf(d1, 0.0, 1.0)-K*np.exp(-r*T)*stats.norm.cdf(d2, 0.0, 1.0)
        if price - (price_implied) < 0.001:
            return sigma
        sigma += 0.001
def implied_volp(price,s0,K,T,r):
    import numpy as np
    from scipy import stats
    sigma=0.01
    while sigma<1:
        S0 = float(s0)
        d1 = (np.log(S0 / K) + (r + sigma ** 2 / 2.) * T) / (sigma * np.sqrt(T))
        d2=(np.log(S0/K) + (r - sigma**2/2.)*T) / (sigma*np.sqrt(T))
        option_pv = (s0 * stats.norm.cdf(d1, 0.0, 1.0)) - (K * np.exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
        price_implied= K*np.exp(-r*T)-s0+option_pv
        if price - (price_implied) < 0.001:
            return sigma
        sigma += 0.001
def buy_market(session, ticker, quantity):
    mkt_buy_params = {"ticker": ticker,
                      "type": "MARKET",
                      "quantity": quantity,
                      "action": "BUY"}
    resp = session.post("http://localhost:9999/v1/orders", params=mkt_buy_params)
    if resp.ok:
        # Step 7: Parse the returned data by calling the json() method:
        mkt_order = resp.json()
        # Step 8: Work with the parsed data:
        id = mkt_order['order_id']  # extract the order id from the object "mkt_order"
        print(f"The market buy order was submitted and has the id {id}")
        return id
    else:
        print("The order was not successfully submitted!")
        return 0
def sell_market(session, ticker, quantity):
    mkt_sell_params = {"ticker": ticker,
                      "type": "MARKET",
                      "quantity": quantity,
                      "action": "SELL"}
    resp = session.post("http://localhost:9999/v1/orders", params=mkt_sell_params)
    if resp.ok:
        # Step 7: Parse the returned data by calling the json() method:
        mkt_order = resp.json()
        # Step 8: Work with the parsed data:
        id = mkt_order['order_id']  # extract the order id from the object "mkt_order"
        print(f"The market sell order was submitted and has the id {id}")
        return id
    else:
        print("The order was not successfully submitted!")
        return 0
