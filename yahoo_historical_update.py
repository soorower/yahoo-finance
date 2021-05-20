import pandas as pd
import time
import sys
import datetime

#    python yahoo_historical_update.py 01-01-2015 19-05-2021    >It will work on any date range<

startTime = time.time()
symbols = pd.read_csv('Symbols.csv')['Symbol'].tolist()
st = sys.argv[1]
en = sys.argv[2]
start = datetime.datetime.strptime(st, "%d-%m-%Y")
end = datetime.datetime.strptime(en, "%d-%m-%Y")

date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
my_dates = []
for date in date_generated:
    my_dates.append('20'+ str(date.strftime("%y-%m-%d")))
my_dates.append(en[-4:]+en[2:6]+en[:2])


date_time = st
pattern = '%d-%m-%Y'
period_1 = str(time.mktime(time.strptime(date_time, pattern))).split('.')[0]
period_2 = str(time.time()).split('.')[0]
lists = []
data = {}
counter = 1
for symbol in symbols:
    print(counter)
    symbol1 = symbol.replace('.','').replace(',','')
    symbol = symbol1[:-1]+'.'+symbol1[-1:]
    counter = counter + 1
    CMP = symbol
    print(CMP)
    links = "https://query1.finance.yahoo.com/v7/finance/download/"+ CMP + "?period1="+ period_1 + "&period2="+ period_2 + "&interval=1d&events=history&includeAdjustedClose=true"
    try:
        df = pd.read_csv(links)
        dates = df['Date'].tolist()
        opens = df['Open'].tolist()
        closes= df['Close'].tolist()
        adj_closes = df['Adj Close'].tolist()
        volumes = df['Volume'].tolist()
        dates.reverse()
        opens.reverse()
        closes.reverse()
        adj_closes.reverse()
        volumes.reverse()
        for date,open,close,adj_close,volume in zip(dates,opens,closes,adj_closes,volumes):
            if date in my_dates:
                try:
                    date = date
                    open = open
                    close = close
                    adj_close = adj_close
                    volume = volume
                except:
                    date = '-'
                    open = '-'
                    close = '-'
                    adj_close = '-'
                    volume = '-'
                data = {
                    'Symbol': CMP,
                    'Date': date,
                    'Open': open,
                    'Close': close,
                    'Adj Close': adj_close,
                    'Volume': volume
                }
                lists.append(data)
    except:
        print(f'This is a wrong symbol: {symbol}')
        pass
df1 = pd.DataFrame(lists).pivot_table(index=['Symbol'],values = 'Close', columns = 'Date').reset_index()
df = df1[df1.columns[::-1]]
columns = df.columns.tolist()
columns = columns[-1:] + columns[:-1]
df = df1[columns]
df.to_csv(f'Yahoo Historical {st} to {en}.csv',encoding='utf-8', index=False)

total_time = str(time.time() - startTime)[:5]
print(f'Finished! It took {total_time}(seconds) to scrape all...')