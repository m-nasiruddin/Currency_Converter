#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen
import pandas as pd


with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
    source = response.read()

print(source)

data = json.loads(source, encoding='utf-8')

print(json.dumps(data, indent=2))

print(len(data['list']['resources']))  # should be 188 resources

data_list = []

for item in data['list']['resources']:
    data_list.append(item['resource']['fields'])

df = pd.DataFrame(data_list)

df.drop(df.columns[[2, 3, 4, 5, 6]], axis=1, inplace=True)

print(df)

print(df[df.name == 'USD/EUR'])

# for item in data['list']['resources']:
#     print(item)
#
# usd_rates = dict()
#
# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price
#
# print(50 * float(usd_rates['USD/EUR']))
