import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#print(8)
#print("hello")
hourly_dataindex=yf.download("^GSPC",start="2023-01-01",end="2024-1-01",interval="1h")
hourly_dataindex.head()
print(hourly_dataindex.head())
hourly_datastock=yf.download("DELL" ,start="2023-01-01",end="2024-1-01",interval="1h")
hourly_datastock.head()
print(hourly_datastock.head())
dfi = hourly_dataindex.groupby(hourly_dataindex.index.date).agg({
    'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last',
    'Adj Close': 'last',
    'Volume': 'sum'
})
dfs = hourly_datastock.groupby(hourly_datastock.index.date).agg({
    'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last',
    'Adj Close': 'last',
    'Volume': 'sum'
})
print(dfi.head())
print(dfs.head())
#cumlative return =CR;
#dfi[ "return" ]=0
#dfi["CR"]=0
#for i in range (len(dfi)
#plt.figure(figsize=(6,6))
#plt.plot(dfi["close"],label="index")
#sns.lineplot(data=dfi)
#import seaborn as sb

#plt.xlabel("Date")
#plt.show()

dfi['return']=0
for i in range(0,len(dfi)):
  dfi['return'][i]=(dfi['Close'][i]-dfi['Close'][i-1])*100/dfi['Close'][i-1]
#print(dfi['Close'][0]):
print(dfi.head())
dfs['return']=0
for i in range(0,len(dfi)):
  dfs['return'][i]=(dfs['Close'][i]-dfs['Close'][i-1])*100/dfs['Close'][i-1]
#print(dfi['Close'][0])
print(dfs.head())
fi=dfi["Close"][0]
fs=dfs["Close"][0]
dfi["CR"]=0
dfs ["CR"]=0

for i in range (0,len(dfi)):
    dfi["CR"][i]=( dfi['Close'][i]-dfi['Close'][0])*100/dfi['Close'][0]
    
    
    
#print(dfi["CR"][i])
print(dfi.head())
for i in range (0,len(dfi)):
    dfs["CR"][i]=( dfs['Close'][i]-dfs['Close'][0])*100/dfs['Close'][0]
print(dfs.head())
plt.figure(figsize=(14,6))
#plt.plot(dfi["return"],label="index")
sns.lineplot(data=dfi['return'], label="return")
sns.lineplot(data=dfi["CR"], label="CR")
plt.legend()
plt.xlabel("DATE")
#plt.ylabel("RETURN")
plt.show()
sns.lineplot(data=dfs['return'], label="return")
sns.lineplot(data=dfs["CR"], label="CR")
plt.legend()
plt.xlabel("DATE")
#plt.ylabel("RETURN")
plt.show()