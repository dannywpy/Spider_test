import csv
import urllib

import pandas as pd

df = pd.read_excel('madelink.xlsx')
parts = df['part']
skus = df['sku']
names= df['name']
f = open('补字母链接.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['link'])
csv_writer.writeheader()
for part,sku,name in zip(parts,skus,names):
    params = (
            ('country', 'USA'),
            ('customerType', 'B2C'),
            ('salesChannel', 'ECOMM'),
            ('preview', 'false'),
            ('lineCode', 'WWD'),
            ('partNumber', part),
            ('vehicleMake',name)
        )
    query_string = urllib.parse.urlencode(params)
    url = f'https://www.autozone.com/external/product-discovery/product/v1/products/{sku}/fitments'
    # 拼接完整的URL
    full_url = f"{url}?{query_string}"


    dit = {
        'link':full_url
    }
    csv_writer.writerow(dit)







