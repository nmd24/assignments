# -*- coding: utf-8 -*-
"""
IB API - Calculating implied volatility using market price of options

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

# Import libraries
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import pandas as pd
import numpy as np
import threading
import time
from scipy import stats
from scipy import optimize

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 
        self.data = {}
        
    def historicalData(self, reqId, bar):
        if reqId not in self.data:
            self.data[reqId] = [{"Date":bar.date,"Open":bar.open,"High":bar.high,"Low":bar.low,"Close":bar.close,"Volume":bar.volume}]
        else:
            self.data[reqId].append({"Date":bar.date,"Open":bar.open,"High":bar.high,"Low":bar.low,"Close":bar.close,"Volume":bar.volume})
        print("reqID:{}, date:{}, open:{}, high:{}, low:{}, close:{}, volume:{}".format(reqId,bar.date,bar.open,bar.high,bar.low,bar.close,bar.volume))
        
    def historicalDataEnd(self, reqId, start, end):
        super().historicalDataEnd(reqId, start, end)
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        event.set()

def usTechStk(symbol,sec_type="STK",currency="USD",exchange="ISLAND"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    return contract 

def histData(req_num,contract,duration,candle_size):
    """extracts historical data"""
    app.reqHistoricalData(reqId=req_num, 
                          contract=contract,
                          endDateTime='',
                          durationStr=duration,
                          barSizeSetting=candle_size,
                          whatToShow='ADJUSTED_LAST',
                          useRTH=1,
                          formatDate=1,
                          keepUpToDate=0,
                          chartOptions=[])	 # EClient function to request contract details

def websocket_con():
    app.run()
    
app = TradeApp()
app.connect(host='127.0.0.1', port=7497, clientId=23) #port 4002 for ib gateway paper trading/7497 for TWS paper trading
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) # some latency added to ensure that the connection is established

event = threading.Event()

tickers = ["AAPL","AMZN","TSLA"]
for ticker in tickers:
    event.clear()
    histData(tickers.index(ticker),usTechStk(ticker),'300 D', '1 day')
    event.wait()
    
###################storing trade app object in dataframe#######################
def dataDataframe(symbols,TradeApp_obj):
    "returns extracted historical data in dataframe format"
    df_data = {}
    for symbol in symbols:
        df_data[symbol] = pd.DataFrame(TradeApp_obj.data[symbols.index(symbol)])
        df_data[symbol].set_index("Date",inplace=True)
    return df_data

#extract and store historical data in dataframe
historicalData = dataDataframe(tickers,app)

    
#################Implied Vol Calculation using optimization####################
def imp_vol_bsm(stock_price,strike_price,option_price,time,rate,right="Call"):
    
    def black_scholes(vol):
        d1 = (np.log(stock_price/strike_price) + (rate + 0.5* vol**2)*time)/(vol*np.sqrt(time))
        d2 = (np.log(stock_price/strike_price) + (rate - 0.5* vol**2)*time)/(vol*np.sqrt(time))
        nd1 = stats.norm.cdf(d1)
        nd2 = stats.norm.cdf(d2)
        n_d1 = stats.norm.cdf(-1*d1)
        n_d2 = stats.norm.cdf(-1*d2)
        if right.capitalize()[0] == "C":
            opt_price = round((stock_price*nd1) - (strike_price*np.exp(-1*rate*time)*nd2),3)
        else:
            opt_price = round((strike_price*np.exp(-1*rate*time)*n_d2) - (stock_price*n_d1),3)
        return option_price - opt_price
    
    return optimize.brentq(black_scholes,0.05,0.9,maxiter=1000)

#calculate historical volatility of each ticker to be fed into black scholes model
imp_vol = {}
current_price = {"AAPL":189.90,"AMZN":146.63,"TSLA":235.70}
strike_price = {"AAPL":195,"AMZN":145,"TSLA":240}
time = 5/365
rate = 0.05
call_price = {"AAPL":0.19,"AMZN":3.15,"TSLA":3.90}
put_price = {"AAPL":5.6,"AMZN":1.25,"TSLA":8.15}


for ticker in historicalData:
    imp_vol[ticker] = imp_vol_bsm(current_price[ticker],
                                  strike_price[ticker],
                                  put_price[ticker],
                                  time, rate, "Put")
    print("Implied vol for underlying {}: {}".format(ticker,round(imp_vol[ticker],3)))
