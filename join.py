# -*- coding: utf-8 -*-
import csv
import io
import re
price = io.open('price.csv', 'r', encoding='utf-8')
merged = open('news_and_price.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(merged)
f_price = csv.reader(price)
h_price = next(f_price)[1:]
print(h_price)  # head

p = next(f_price)
with io.open('news_merged.csv', 'r', encoding='utf-8') as f:
    f_news = csv.reader(f)
    h_news = next(f_news)[:-3]
    print(h_news)  # head
    writer.writerow(h_news + h_price[1:])
    # pre compile to boost speed
    reg = re.compile(
        r'^(\[?)(([0-9]{1,}(-|\.|\/)[0-9]{1,}(-|\.|\/)[0-9]{1,})|([0-9]{8}))(\]?)')
    index = 0
    for r in f_news:
        index += 1
        if(len(r[2]) == 0):
            break
        while(p[1] != r[1]):
            p = next(f_price)
        # print(p[1], r[1], 'index: ', index)
        # remove date in subject
        r[2] = reg.sub('', r[2])
        # Merge price and news by date
        writer.writerow(r[:-3] + p[2:])
