# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import time
import datetime
import json
interval = '1'
d = datetime.date(2021,9,5)
start = str(time.mktime(d.timetuple()))[:-2]
d = datetime.date(2021,9,14)
end = str(time.mktime(d.timetuple()))[:-2]
#Id say try using GMT
end = '1631563200'
print(time.ctime(int(end)))
ticker = 'AAPL'
APIkey= 'c4rrfr2ad3ic8b7crong'
url = 'https://finnhub.io/api/v1/stock/candle?symbol='+ticker+'&resolution='+interval+'&from='+start+'&to='+end+'&token='+APIkey
with urllib.request.urlopen(url) as response:
   data = response.read()
data = data.decode('utf-8')
data = json.loads(data)
for i in range(len(data['t'])):
    data['t'][i] = datetime.datetime.strptime(time.ctime(data['t'][i])[4:],'%b  %d %H:%M:%S %Y')
for i in reversed(data['t']):
    if not(i > i.replace(hour=6,minute=30) and i < i.replace(hour=13,minute=0)):
        index = data['t'].index(i)
        for item in data:
            try:
                data[item].remove(data[item][index])
            except:
                print('I tried')
            