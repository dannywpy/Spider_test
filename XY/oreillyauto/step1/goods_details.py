import csv
import random
import threading
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()
f = open('production_information.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['part','information','link'])
csv_writer.writeheader()
headers = {
        'User-Agent': ua.random
        ,'Cookie':'trcksesh=64f32212-129e-4c32-8853-84d9ea317bf9; uws_storage=%22cookie%22; __wid=164969602; __pdst=4bc079921c39473f943b7ccfb242a57a; _fbp=fb.1.1717507284190.249225726405179591; _gid=GA1.2.1457245848.1717507285; LPVID=ljOGQzOWQxZWZhZTg1YWU3; selectedStoreId=5545; truyoConsent={"consumerCookieId":"334f1878-8484-476d-bb9e-da18b446713d","displayCookieBar":"true","flag":1}; uws_story_Orellyauto_Browse=%7B%22done%22%3Afalse%2C%22stopped%22%3Atrue%7D%7C1720099915113; RT="z=1&dm=oreillyauto.com&si=xl0b23zg6o&ss=lx0fl9nh&sl=d&tt=jw4&obo=6"; NoCookie=true; JSESSIONID=CE53D53D81E1D99325D64C09F4431070; ga_session=2cc078a0-4615-4599-8a0a-b64c16691921; ActiveID=ZOSA-GD1G-OSHF-VGJA-HHHS-JSJZ-TWX3-7WY0; cust_id="Q+4MEM7m5vVUoGEJQ+OEGpHHrFTMP+UAwH3aXIMUBPE="; OSESSIONID="9d4ef42cf67b0a3c"; uws_prop_8swyp7jh=%22N%2FA%22%7Csession_timeout; uws_prop_5lcxgghj=%22N%2FA%22%7Csession_timeout; uws_prop_q8ub7x2l=%22N%2FA%22%7Csession_timeout; uws_prop_vn35otqo=%22N%2FA%22%7Csession_timeout; uws_prop_8jo1u2t0=%222cc078a0-4615-4599-8a0a-b64c16691921%22%7Csession_timeout; uws_prop_w71w8mxp=%225545%7C1590%20S%20Main%20St%7CWillits%7CCA%22%7Csession_timeout; uws_rate_comparators=%7B%22global%22%3A3183313%7D%7Csession_timeout; BVImplmain_site=14810; uws_recording=%7B%22status%22%3A%22recording%22%2C%22conditional%22%3Atrue%2C%22requestActivation%22%3Afalse%2C%22recordingType%22%3Anull%7D%7Csession_timeout; LPSID-16349016=fTUvz0tyTMapsJHyJ4YhuQ; uws_session=%7B%22start%22%3A1717594474315%2C%22count%22%3A6%2C%22referrer%22%3A%22%22%7D%7Csession_timeout; uws_visitor=%7B%22vid%22%3A%22171750728394821536%22%2C%22start%22%3A1717507283948%2C%22count%22%3A49%7D%7C1725372056847; _abck=CF755594DDF57659D5FFC58514992E49~0~YAAQTZZUaI2mzb6PAQAAmPiz6Azb1Pjgr5zX2EuVNql7ey3FeMaZEeDm6JN2MlbNdIeCyMBB68o+lUapbEXBbT5uokDs1AytcjfHyCvq28d8xUenzBx4jNzc96GEWMKI3XFtNF5CfulacS6HbRVAVSftd8nmn0mHUfTu0dThDPVlrEhCSVAb+N2DWpR2/qQMAzkK7hEWOdCmKcqvOQChqDGeZo4BjCCkqI6DfuOaFGrAMIfWXm2dWHem76NzPqZO0ypugtjWHPla8P5IZEeJFxVVnQbhhiHfRne99zUq12PYou9qvQF4PROwuB6DYySmjaTUh+hxTU6Wix54QOVqFzJ501ml8tvh3nqbEHqHq7S5U7C2xFTf1piup2Y8jHuquH4a4nrkmOY+q+vXAf92ygNyxgiSshCbP7vJ1jI=~-1~-1~-1; bm_sz=A4BCFC26EF2CC457E9D2C8F7ED049643~YAAQTZZUaI6mzb6PAQAAmPiz6BhCwNUXh9kBfzKvT9DBNv3kRJIZ5Xm0wLbGamI5u8AyayhISjicFXdTzW4Osx9FT753wu2Q+7PI7l19hGaqrzQzfJ3/Rd6d+G5YR/pkHkkbyhBurjDyB+VzWQnKj3iaizn7oKmtBYzdy4lNrK8ByYruP6AR4IHfO2J93t7HNH6uspOAL3WeaGfj5g8fOttcL1B/RspKnyj0VIJmNsFpVLwMoz2fiqfzRR3ziP3f/bjHQ1+uEP7kE43qZfuoAQ7+GLAFY9LiRRzfESHS2GwWuKuMJ/+SRpSlWi8/M/KE2I/GTKOytzOm+N+FGTTZrT0HoOHUQTMIy8fd16RU0gTu1hTrxseJxd9hhe0=~4277555~4276532; EPCRVP="ULT-R612249A,dad3c6651e74|ULT-R612302A,dad3c6651e74|WIL-71-25-18301,dad3c6651e74|ULT-R612268A,dad3c6651e74|USL-N612453A,dad3c6651e74|USL-N612617A,dad3c6651e74"; forterToken=e52ece034bed405b863fa4a29e77f3fd_1717596918066_454_UDF43-mnf_13ck; fs_lua=1.1717596922152; fs_uid=#o-1TY56E-na1#247ac87c-6514-4674-90ef-5871c9d7088e:6348bbed-6afe-4a4b-a1c4-61150cfac1cd:1717594474572::7#/1749043389; _ga=GA1.2.261699399.1717507284; _ga_TV3LS85R98=GS1.1.1717594472.4.1.1717597177.0.0.0'
    }
df = pd.read_excel('links.xlsx')
links = df['ln']

for url in links:

    time.sleep(random.uniform(1,5))
    response = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    part = soup.find(class_='lineNumber js-ga-product-line-number')
    productions = soup.find_all(class_='col-md-6')
    try:
        for production in productions:
            dit = {
                'part':part.text.strip(),
                'information':production.text.strip(),
                'link':url
            }

            csv_writer.writerow(dit)

        print(f'suddessfully++++++++=========================')

    except AttributeError:
        print(f'fail{url}')






