# P1.1 Download Hourly Data

    1. used yf.download to download data of bosch share and SnP500 index

# P1.2 Convert Horly To Daily

    1. not able to understand the adj close right now ho
    2. code will break if the data type is not date
        # df.dtypes['Datetime']
        # df['Datetime'] = pd.to_datetime(df['Datetime']) if needed

# P1.3 Daily and Cumulative Return

    1. Bosch Share's dialy return were very
    high multiple time through-out the year.
    2. SnP 500 were comparatively constant on daily
    3. over the year as cumulative return bosch won the race, the same time bosch was a bt risky as it at some points offered very high negative returns.

# P2.1 Download Daily Data

    1. apple data using yf.Ticker

# P2.2 Caluclated New Datetime attribute

    1. Friday was the day of max close for 15 weeks, and monday for 12, followed by Thrusday for 11 weeks, over the year.

# P2.3 7-day Rolling Mean

    1. as a inside, i have calculated the 7-day and 14-day rolling mean, and tried to make a indicator similar to MACD, and have found the period of bullish and bearish maket trends.

# and i was a bit unsure what i have to write in this readme.
