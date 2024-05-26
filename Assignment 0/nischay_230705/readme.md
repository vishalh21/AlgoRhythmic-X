## ASSIGNMENT0

### PROBLEM1 
##### PARTA
1. Downloading hourly data from January2023 to January2024(including both months)

2. Using yf.Ticker() to do so



##### PARTB
1. Dropping Divends and Stock Split as they will not take part in final calculations

2. Using resample by day making the dataframe of daily 

##### PARTC

1. FOR DAILY RETURN: (obj["Close"]-obj["Open"])/obj["Open"])*100

2. FOR CUMULATIVE RETURN: ((obj["Close"]-obj["Open"][0])/obj["Open"][0])*100

3. Plotting shows that as stock changed, it affected index also which it should as NVDIA is 3rd largest stock in sp500


### PROBLEM2
##### PARTA
1. Simply just downloading data by .Ticker() method

2. In history choosing interval='1d'

3. Dropping Dividends and Stock splits 

##### PARTB

1. StockExchange closed on Saturday and Sunday

2. Plotting avg on each day

3. **Highest Closing price for **TUESDAY****

##### PARTC

1. Filling the first 6 days with nan values and then dropping them because it is 7 day moving average

2. I have commented the code for VARIABLE SIZE window in the initial 6 days, which adds averg of as many days before it(for <7 days).

3. Plotting data we see an averaging effect with lag 


