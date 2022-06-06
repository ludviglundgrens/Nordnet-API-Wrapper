from ast import Try
import json
import csv
import time
import requests

f = open('tickers.csv', 'w')

# Init Nordnet session
s = requests.Session() 
res = s.post('https://www.nordnet.se/api/2/login/anonymous',
            headers = {
                'Content-Type': 'application/json',
            }) 

# Fetch instrument data structure
res = s.get('https://www.nordnet.se/api/2/instrument_search/query/stocklist?limit=100&offset=0')
j = json.loads(res.content)
instr = j['results'][0]['instrument_info']

# Extract column names 
names = []
for i in instr:
    names.append(i)

# Setup writer  
writer = csv.writer(f)
writer.writerow(names)

# Loop through all stocktickers
total_hits =  j['total_hits']
i = 0
while i < total_hits:
    url = "https://www.nordnet.se/api/2/instrument_search/query/stocklist?limit=100&offset=" + str(i)
    res = s.get(url)
    out = json.loads(res.content)
    for j in range(0,99):
        try: 
            instr = out['results'][j]['instrument_info']
            row = []
            for key in instr:
                row.append(instr[key])
            writer.writerow(row)
        except: 
            print("Index out of range")
    i += 100
    time.sleep(2)
    print("Fetched", i, "tickers of", total_hits)

# Loop through all etf tickers
url = "https://www.nordnet.se/api/2/instrument_search/query/etflist?sort_order=desc&sort_attribute=yield_1y&limit=100"
res = s.get(url)
j = json.loads(res.content)
total_hits =  j['total_hits']
i = 0
while i < total_hits:
    url = "https://www.nordnet.se/api/2/instrument_search/query/etflist?sort_order=desc&sort_attribute=yield_1y&limit=100&offset=" + str(i)
    res = s.get(url)
    out = json.loads(res.content)
    for j in range(0,99):
        try: 
            instr = out['results'][j]['instrument_info']
            row = []
            for key in instr:
                row.append(instr[key])
            writer.writerow(row)
        except: 
            print("Index out of range")
    i += 100
    time.sleep(1)
    print("Fetched", i, "tickers of", total_hits)
