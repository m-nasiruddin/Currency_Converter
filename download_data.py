#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen
import pandas as pd


with urlopen('https://free.currencyconverterapi.com/api/v5/currencies') as response:
    source = response.read()

print(source)

data = json.loads(source, encoding='utf-8')

print(json.dumps(data, indent=2))

df = pd.DataFrame(data['results'])

print(df)

print(df.loc['id'])

print(len(df.loc['id']))  # should be 156 currencies

df_list = df.loc['id'].tolist()

for item in df_list:
    print(item)

with urlopen('https://free.currencyconverterapi.com/api/v5/convert?q=USD_PHP&compact=ultra') as response:
    destination = response.read()

print(destination)

#
# for item in data['results']['id']:
#     print(item)
