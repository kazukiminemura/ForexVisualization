import urllib
import json
from pprint import pprint
import pygame

import numpy as np
import matplotlib.pyplot as plt




fig, ax = plt.subplots(1, 1)
x = 0
y = 0
lines, = ax.plot(x, y)

x = np.zeros(1)
y = np.zeros(1)
# main loop
#clock = pygame.time.Clock()
clock = 1
while True:
    #clock.tick(0.1)


    # GET YQL VIA yahooapis
    url = "https://query.yahooapis.com/v1/public/yql"
    params = {
        "q": 'select * from yahoo.finance.xchange where pair in ("GBPUSD")',
        "format": "json",
        "env": "store://datatables.org/alltableswithkeys"
    }
    url += "?" + urllib.urlencode(params)
    res = urllib.urlopen(url)
    # receive the results in json format
    result = json.loads(res.read().decode('utf-8'))
    #pprint(result)
    #"""
    #{'query': {'count': 1,
    #           'created': '2016-08-22T02:57:07Z',
    #           'lang': 'en-US',
    #           'results': {'rate': {'Ask': '100.6850',
    #                                'Bid': '100.6380',
    #                                'Date': '8/21/2016',
    ##                                'Name': 'USD/JPY',
    #                                'Rate': '100.6380',
    #                                'Time': '10:58pm',
    #                                'id': 'USDJPY'}}}}
    #"""

    # get requried information (USD/JPY: this time)
    rate = result["query"]["results"]["rate"]["Rate"]
    #print('GBP/USD:', rate)
    # USD/JPY: xxx.xx

    clock += 1
    x.append(clock)
    y.append(float(rate))

    #print len(x)
    if len(x) > 10:
        x = x[1:]
        y = y[1:]

    plt.plot(x, y)
    #lines.set_data(np.asarray(x), np.asarray(y))
    ax.set_xlim((x.min(), x.max()))
    plt.pause(1)
