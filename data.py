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
ticker = 'AAPL'
APIkey= 'c4rrfr2ad3ic8b7crong'
url = 'https://finnhub.io/api/v1/stock/candle?symbol='+ticker+'&resolution='+interval+'&from='+start+'&to='+end+'&token='+APIkey
with urllib.request.urlopen(url) as response:
   data = response.read()
data = data.decode('utf-8')
data = json.loads(data)