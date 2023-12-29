import requests
import json
url = 'https://deindex.h3c.com/API/AllCityOneInfo.ashx?callback=jQuery112305266678590531533_1703424271944'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'


         }

response = requests.get(url=url,headers=headers)

data = response.text



print(data)














