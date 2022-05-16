import json
import csv
import string

ids = []
names = []
symbols = []
isins = []
with open('./data.json') as data:
    df = json.load(data)
    for i in range(0,len(df)-1):
        res = df[i]['results']
        for j in range(0,len(res)-1):
            row = res[j]['instrument_info']
            id = row['instrument_id']
            name = row['name']
            symbol = row['symbol']
            isin = row['isin']

            ids.append(id)
            names.append(name)
            symbols.append(symbol)
            isins.append(isin)

f = open('tickers.csv', 'w')
writer = csv.writer(f)

for i in range(0, len(ids)-1):
    s = [str(ids[i]), str(names[i]), symbols[i], isins[i]]
    writer.writerow(s)