# -*- coding: utf-8 -*-
"""
IB API - Monte Carlo simulation for pricing options

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
import matplotlib.pyplot as plt

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

#################Monte Carlo Option pricing Model############################

#calculate historical volatility of each ticker to be fed into black scholes model
hist_vol = {}

call_price = {}
put_price = {}
current_price = {"AAPL":189.90,"AMZN":146.63,"TSLA":235.70}
strike_price = {"AAPL":195,"AMZN":145,"TSLA":240}
time = 5/365
rate = 0.0535
num_ts = 50
num_path = 1000

def monte_carlo(stock_price,strike_price,vol,time,rate,right="Call"):
    paths = []
    for i in range(num_path):
        path = [stock_price]
        for j in range(num_ts):
            price_new = path[j] * np.exp((rate - 0.5* vol**2)*(time/num_ts) + vol*np.sqrt(time/num_ts)*np.random.normal())
            path.append(price_new)
        paths.append(path)
    
    payoff = 0
    for path in paths:
        if right.capitalize()[0] == "C":
            payoff+=max(path[-1] - strike_price,0)
        else:
            payoff+=max(strike_price - path[-1],0)
    
    return (payoff/num_path)*np.exp(-1*rate*time)

def monte_carlo_with_graph(stock_price,strike_price,vol,time,rate,right="Call"):
    #caution - slows dows option pricing
    paths = []
    for i in range(num_path):
        path = [stock_price]
        for j in range(num_ts):
            price_new = path[j] * np.exp((rate - 0.5* vol**2)*(time/num_ts) + vol*np.sqrt(time/num_ts)*np.random.normal())
            path.append(price_new)
        paths.append(path)
    
    #plotting paths
    plt.xlabel("time step")
    plt.ylabel("stock price evolution of {}".format(ticker))
    plt.title("monte carlo simulation")
    for i in range(len(paths)):
        plt.plot([x for x in range(len(paths[0]))],paths[i])
    plt.legend()
    plt.show()
       
    payoff = 0
    for path in paths:
        if right.capitalize()[0] == "C":
            payoff+=max(path[-1] - strike_price,0)
        else:
            payoff+=max(strike_price - path[-1],0)
    
    return (payoff/num_path)*np.exp(-1*rate*time)


for ticker in historicalData:
    historicalData[ticker]["return"] = historicalData[ticker]["Close"].pct_change()
    hist_vol[ticker] = historicalData[ticker]["return"].std()*np.sqrt(252)
    call_price[ticker] = monte_carlo(current_price[ticker],
                                       strike_price[ticker],
                                       hist_vol[ticker],
                                       time, rate, "Call")
    put_price[ticker] = monte_carlo(current_price[ticker],
                                       strike_price[ticker],
                                       hist_vol[ticker],
                                       time, rate, "Put")

