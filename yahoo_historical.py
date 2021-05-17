import pandas as pd
import time
import sys
import datetime
startTime = time.time()
symbols = pd.read_csv('Symbols.csv')['Symbol'].tolist()[:1]

st = sys.argv[1]
en = sys.argv[2]
start = datetime.datetime.strptime(st, "%d-%m-%Y")
end = datetime.datetime.strptime(en, "%d-%m-%Y")

date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
my_dates = []
for date in date_generated:
    my_dates.append('20'+ str(date.strftime("%y-%m-%d")))
my_dates.append(en[-4:]+en[2:6]+en[:2])
# print(my_dates)
lists = []
data = {}
counter = 1
for symbol in symbols:
    print(counter)
    counter = counter + 1
    CMP = symbol
    print(CMP)
    links = "https://query1.finance.yahoo.com/v7/finance/download/"+ CMP + "?period1=1589618009&period2=1621154009&interval=1d&events=history&includeAdjustedClose=true"
    df = pd.read_csv(links)
    dates = df['Date'].tolist()
    opens = df['Open'].tolist()
    closes= df['Close'].tolist()
    adj_closes = df['Adj Close'].tolist()
    volumes = df['Volume']
    
    for date,open,close,adj_close,volume in zip(dates,opens,closes,adj_closes,volumes):
        # print(date)
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
df1 = pd.DataFrame(lists)
df = df1.reset_index(drop=True)
df.to_csv(f'Yahoo Historical {st} to {en}.csv',encoding='utf-8', index=False)

total_time = str(time.time() - startTime)[:3]
print(f'Finished! It took {total_time}(seconds) to scrape all...')