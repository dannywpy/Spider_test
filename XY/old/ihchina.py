import codecs

import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',

}
resp = requests.get(url='https://aiida.materialscloud.org/curated-cofs/discover/detail?mat_id=2245rN2',headers=headers)
print(resp.text)
















