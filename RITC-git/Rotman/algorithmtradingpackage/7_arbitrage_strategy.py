import signal
import requests
from time import sleep


# We first build a class which will print error messages and will stop the program whenever we need it to:
class ApiException(Exception):
    pass


# Whenever Ctrl+C is pressed, the algorithm shuts down:
def signal_handler(signum, frame):
    global shutdown
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    shutdown = True


API_KEY = {"X-API-key": "ZXZH6DVX"}
shutdown = False


# we create a helper method to return the current tick of the running case:
def get_tick(session):
    resp = session.get("http://localhost:9999/v1/case")
    if resp.ok:
        case = resp.json()
        return case["tick"]
    raise ApiException("Authorization error! Please check API key!")


# Now we create a helper method to get the bid and ask for a given security:
def ticker_bid_ask(session, ticker):
    payload = {"ticker": ticker}
    resp = session.get("http://localhost:9999/v1/securities/book", params=payload)
    if resp.ok:
        book = resp.json()
        bid = book["bids"][0]["price"]
        ask = book["asks"][0]["price"]
        return bid, ask
    raise ApiException("Authorization error! Please check API key!")


# Helper function to place a market order::
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
        global reminder
        reminder = True
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

# helper function to place a limit order:
def buy_limit(session, ticker, quantity, price):
    lmt_buy_params = {"ticker": ticker,
                       "type": "LIMIT",
                       "quantity": quantity,
                       "action": "BUY",
                       "price": price}
    resp = session.post("http://localhost:9999/v1/orders", params=lmt_buy_params)
    if resp.ok:
        lmt_order = resp.json()
        id = lmt_order["order_id"]
        print(f"The limit buy order was submitted successfully with ID: {id}")
        return id
    else:
        print("The order was not successfully submitted!")
def sell_limit(session, ticker, quantity, price):
    lmt_sell_params = {"ticker": ticker,
                       "type": "LIMIT",
                       "quantity": quantity,
                       "action": "SELL",
                       "price": price}
    resp = session.post("http://localhost:9999/v1/orders", params=lmt_sell_params)
    if resp.ok:
        lmt_order = resp.json()
        id = lmt_order["order_id"]
        print(f"The limit sell order was submitted successfully with ID: {id}")
        return id
    else:
        print("The order was not successfully submitted!")


# helper function to place a market sell order:

def is_security_open(ticker):
    with requests.Session() as s:
        s.headers.update(API_KEY)
        resp = s.get("http://localhost:9999/v1/securities")
        if resp.ok:
            status = resp.json()
            for stock in status:
                if stock['ticker'] == ticker and stock['position'] > 0:                   return True
            return False
        else:
            print("The resp is not OK")

def is_security_open2(ticker):
    with requests.Session() as s:
        s.headers.update(API_KEY)
        resp = s.get("http://localhost:9999/v1/securities")
        if resp.ok:
            status = resp.json()
            for stock in status:
                if stock['ticker'] == ticker and stock['position'] < 0:                   return True
            return False
        else:
            print("The resp is not OK")

# MAIN() Method:
def main():
    with requests.Session() as s:
        s.headers.update(API_KEY)
        tick = get_tick(s)
        initial_money = 10000000
        num_bull = 0
        num_bear = 0
        num_etf = 0
        


        while tick > 5 and tick < 295 and not shutdown:
            # IMPORTANT: It is imp. to update the tick at the end of the loop to check that the algorithm should still run or not
            tick = get_tick(s)
            usd_bid, usd_ask = ticker_bid_ask(s, "USD")
            cad_bid, cad_ask = ticker_bid_ask(s, "CAD")
            bull_bid, bull_ask = ticker_bid_ask(s, "BULL")
            bear_bid, bear_ask = ticker_bid_ask(s, "BEAR")
            etf_bid, etf_ask = ticker_bid_ask(s, "RITC")

            # Portfolio Constraints and Markey Dynamics:
            cad_bid, usd_max = 2500000, 2500000
            bull_max, bear_max, ritc = 10000, 10000, 10000
            market_order_fee = 0.02
            limit_order_rebate = 0.01
            """
            USD = x means we need x number of CAD to buy 1 USD
            BULL -> CAD
            BEAR -> CAD
            ETF  -> USD => ETF_CAD = ETF/USD_BID
            """
            # Trading Strategy:
            etf_bid_cad = usd_bid * etf_bid
            etf_ask_cad = usd_ask * etf_ask
            quantity = 10000

            bear_ask_usd = bear_ask/usd_bid
            bull_ask_usd = bull_ask/usd_bid
            

# check here
            
            if (bear_ask_usd + bull_ask_usd)+2*market_order_fee > etf_ask: #underpriced
                if not is_security_open("RITC"):
# or check here
                    buy_limit(s, "RITC", quantity, etf_ask)
                    sell_limit(s, "RITC", quantity, etf_ask*1.01+0.02)
                    print(f"Buy: {quantity} 'RITC' @ {etf_ask},\t Sell: {quantity} @ {etf_ask*1.01+0.02}")
            sleep(0.3)
            if (bear_ask_usd + bull_ask_usd)+2*market_order_fee < etf_ask:
                if not is_security_open2("RITC"):
                    sell_market(s, "RITC", quantity)
                    buy_limit(s, "RITC", quantity, etf_bid*0.99+0.02)
                    print(f"Sell: {quantity} 'RITC' @ {etf_bid},\t Buy: {quantity} @ {etf_bid*0.99+0.02}")
            sleep(0.3)
    
if __name__ == '__main__':
    # register the custom signal handler for graceful shutdowns:
    signal.signal(signal.SIGINT, signal_handler)
    main()

API_KEY = {'X-API-key': "57P2J5MY"}
shutdown = False


# this helper method returns the "tick" of the running case:
def get_tick(session):
    resp = session.get()
