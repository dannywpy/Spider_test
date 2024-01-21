import re

import pandas as pd
import matplotlib.pyplot as plt
import time
import openpyxl
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
ua = UserAgent()


headers = {
'User-Agent': ua.random,
    'Cookie':'__mta=220552871.1716380370951.1716380404654.1716383162633.9; uuid_n_v=v1; uuid=89F5DEE0183511EFA7D89144D35F720D0AF124EB6E4F4B3882286D2DB401DAB9; _csrf=1af015def3dfdccd4f2082966b1f65244a197f8076deeccdd023bd196877d1e5; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1716380371; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=18fa03e073bc8-08831fef0c7635-26001d51-240000-18fa03e073bc8; _lxsdk=89F5DEE0183511EFA7D89144D35F720D0AF124EB6E4F4B3882286D2DB401DAB9; __mta=220552871.1716380370951.1716380384902.1716380404654.8; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1716383162; _lxsdk_s=18fa068a092-992-a42-85%7C%7C2'
}
response = requests.get('https://www.maoyan.com/films?sourceId=2&yearId=18&showType=3',headers=headers).text
soup = BeautifulSoup(response, 'html.parser')

links = soup.select('#app > div > div.movies-panel > div.movies-list > dl > dd > div.movie-item.film-channel > a')


















