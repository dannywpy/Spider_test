import csv
import json
import time
import urllib

import pandas as pd
import requests


df = pd.read_excel('ABC.xlsx')
parts = df['part']
skus = df['sku']
f = open('ABC_makes数字.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['name','count','link'])
csv_writer.writeheader()
headers = {

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cookie':'akacd_default=2147483647~rv=45~id=ac196788baf1103ed97aeac8c711f555; TLTSID=853553f6afbc16549e0400e0ed6ab7dd; TLTUID=853553f6afbc16549e0400e0ed6ab7dd; az_bt_cl=hPp0YAbH2l1Jzlm4TTBcIYdKkuXtQB2w06/Qokqu4J+m+8m3MsrmVrDziHlFS1Qx; az_bt_al=0377fda23fd6f17a63fed94298c1ab80; _pxhd=aa364eeaaa7c5abac8676d95d211ca8791d41d1b371d5326874e7e8f310f6a72:02ede793-270e-11ef-a818-3588b0dfcfe5; _pxdc=100; _abck=6F93F75B63D5282BF3569061B34B9E59~-1~YAAQlgcsF1ONNvuPAQAA8c6IAQz2ey2TgwFp6SXXQuCEx9+tGb5ldz7STGwQYw9rNWS+jiNEh7zq3yhw5VcYe4j7D2qp8O4QSaeh24yQoeleotaAKVA59KOVYXIyop4mRlnjDCoCDxWRu9sh9i7aQGOrLTsRMgsrDwvFlKhKaGSGOpGzfKxeDIUfObErTofb/it7ghOwvjmFjLAyQhKYYWAD/7H3eeesBjMdJuH3iyzhJUAMmucyp4h7Hl6BojJo7m6rg7YJVqgfvc6iwUqD+MehBnPlj4TF9T5ufukLiWe6Vk3CEk+A49EyK/ORoETW7Z4EFLtrFqoP6KsyUSHl0cuh5SgOZ+hSiZByErYjzgHqbACA5DEr1GbTxIBrwHU=~-1~-1~-1; sbsd=s/ZA1TMUU91w6Qw49R3VdDaQW0/o3tKWw4OP8a63USuR2/s5cQPq5eCinJrhxhCuG8l+dE8iHPiAJFq1KoplzfuHEs08BDAWlPZNhl1IlyCqDqQRDoO/WMF2/m0VxgqfNAB/fsQ5fzoJJwA3qOO4jl0DJFPY8V2OkiZp4bp3e/iPIpCQ9e4P7mtQa4yCS2LML; sbsd_ss=ab8e18ef4e; ak_bmsc=D8C8AF594B61571C355C012695709177~000000000000000000000000000000~YAAQlgcsF1AvQfuPAQAASxH9ARgX0LHBFIFC6MbZtqg4SXOFPZPHeYB8PMBqm5LDK8AFhuGslisPZ6p/ZL49wG03EhDnRV3NQ3IxWmEDvMBs5ak8MPfscwDhLV993ZihZq14gJOVQxcrVbLeMlcvPKdwYt9+e1qqmsBlpw14RzpoR0QjW+G8k2skjRAcxJRqsi7sHgbXcMulIm1695rvfXz4cRVfnU6mGwdRQ6CoCQvXtDAFba0IZWrLIZraaq6z+Oh0PTMvTGccXaO0k1O4jyYpwSvfiSLvxPQGjey5ztqwAtax+sftaciHGPqCBzmDLgNg/VX9t6NJXmuUdLGxl4oyJ6FZnGLF1TlIijd8ai3CJl5yicaYFD2gUDB5298DdtftPC6/MU38rZyG5w==; bm_sz=6C778223DA0FCE5524C226F694208283~YAAQlgcsF1EvQfuPAQAASxH9ARhOHImB3soS6SCSnwJpsrMbWFWitoHZUveVzDshnIIDZtHQUBEMOwY69p5MBldBPHhFsFRWRWfZyQsYm6mNjK3OKdlEaRMTvLJKF1onMrB6m/4EHfLXC3XGTB5ejV6PjKSTUrKphTLIl4GVPg2yog5qUysPyagC+DFiGfLmiXQ6Mt/TTCuw8mrtP4/TA7iImUPaiegNJwvqcJbanjqJvb/v0PelB99IXYTlJkB11Ci/UOhm8YWIVxjp7HHcudozNAgUqU5GonjFeQKTHDBjfeBMhFRBORm6/H2iFDDKQVcnvbatU3hrGZD+7tnKJ8rav+KjXBVeVotxRoVlyh9dR2KlQxVycvg/xUe2LGSyu6PHhBVpQmP9OGwEasQLTYrVqp7Z/6ZVzFjBWSeJfeeQSA==~4600130~3621698'
}
for part,sku in zip(parts,skus):
    params = (
        ('country', 'USA'),
        ('customerType', 'B2C'),
        ('salesChannel', 'ECOMM'),
        ('preview', 'false'),
        ('lineCode', 'WWD'),
        ('partNumber', part),
    )
    query_string = urllib.parse.urlencode(params)
    url = f'https://www.autozone.com/external/product-discovery/product/v1/products/{sku}/fitments'
    # 拼接完整的URL
    full_url = f"{url}?{query_string}"

    print(full_url)
    time.sleep(1)
    response = requests.get(url=full_url, headers=headers)
    print(response.text)
    json_data = json.loads(response.text)

    for data in json_data:
        print(data['name'])
        print(data['count'])
        dit = {
            'name':data['name'],
             'count':data['count'],
            'link':url
        }
        csv_writer.writerow(dit)
    print(url)




