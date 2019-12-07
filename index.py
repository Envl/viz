# -*- coding: utf-8 -*-
import csv
import io
import re
import json


indexDate = 0
f_json = {}
counter = {}
with io.open('news_and_price.csv', 'r', encoding='utf-8') as f:
    nnp = csv.reader(f)
    index = 0
    print(next(nnp))  # head
    for r in nnp:
        index += 1
        date = r[1]
        if indexDate != date:
            indexDate = date
            f_json[indexDate] = []  # {'count': 0, 'data': []}
            counter[indexDate] = 0
        f_json[indexDate].append({
            'subject': r[2],
            'user': r[3],
            'replies': r[4],
            'views': r[5],
            'price': r[6],
            'open': r[7],
            'high': r[8],
            'low': r[9],
            'vol': r[10],
            'change': r[11]
        })
        counter[indexDate] += 1

print(type(f_json))
for k in f_json:
    print(k, counter[k])

with open('news_by_date.json', 'w', encoding='utf-8') as f:
    json.dump(f_json, f)
with open('news_count.json', 'w', encoding='utf-8') as f:
    json.dump(counter, f)
