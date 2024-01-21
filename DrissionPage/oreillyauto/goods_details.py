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
        ,'Cookie':'__wid=645580747; uws_storage=%22cookie%22; __pdst=73f2387d63334c76a7a6e81f9f9f3422; _gid=GA1.2.1914867437.1717474116; _fbp=fb.1.1717474115734.563557684118401716; LPVID=k5M2NlMTU4YzExNTc0ZDNm; uws_story_Orellyauto_Browse=%7B%22done%22%3Afalse%2C%22stopped%22%3Atrue%7D%7C1720066330285; truyoConsent={"consumerCookieId":"6268abd1-8ef3-4672-a56c-95be5441a034","displayCookieBar":"true","flag":1}; selectedStoreId=2794; OSESSIONID="c0fa4d5df0c7f730"; ga_session=6049bdfd-e2b5-4c26-93c7-136b42645b73; uws_prop_8swyp7jh=%22N%2FA%22%7Csession_timeout; uws_prop_5lcxgghj=%22N%2FA%22%7Csession_timeout; uws_prop_q8ub7x2l=%22N%2FA%22%7Csession_timeout; uws_prop_vn35otqo=%22N%2FA%22%7Csession_timeout; uws_prop_8jo1u2t0=%226049bdfd-e2b5-4c26-93c7-136b42645b73%22%7Csession_timeout; uws_prop_w71w8mxp=%222794%7C1133%20East%20Main%20Street%7CBarstow%7CCA%22%7Csession_timeout; uws_rate_comparators=%7B%22global%22%3A5777277%7D%7Csession_timeout; uws_recording=%7B%22status%22%3A%22recording%22%2C%22conditional%22%3Atrue%2C%22requestActivation%22%3Afalse%2C%22recordingType%22%3Anull%7D%7Csession_timeout; LPSID-16349016=BjWORHMRTceKvahtSass8g; BVImplmain_site=14810; JSESSIONID=76BCEA7B348CB4AF4A53EB215426ED11-n1; ActiveID=PXRO-LLFQ-L4G9-DQLQ-SW7N-YJ4Z-8TFX-H7TO; cust_id="LR0auDrlAoQohJO3Ofr6xuNtqsbKYaGBhEsuOm+xoL4="; EPCRVP="ACD-336-1817,dad3c6651e74|USL-N612503A,dad3c6651e74|USL-N612453A,dad3c6651e74|USL-N612831A,dad3c6651e74|USL-N612617A,dad3c6651e74|USL-N612629A,dad3c6651e74"; dtCookie=v_4_srv_1_sn_E40E089B5DC6F9120287C37C1B7B5AE1_perc_33469_ol_1_app-3A200c4c21b0fea6c6_0; akacd_ost-prod-lb-2=1717679872~rv=38~id=c9f547790d7f76e8219692fa7a010457; _abck=538C548F931A5B6C005F1FAB7BA0B6BB~0~YAAQS1LNF/d4FMKPAQAAaasf6wwV27syrNEJngPNsAbxb7BLQ5dXIb0LEQmVNBGgCPbec4r3JwFHFeNzkyAAjpDifhRcxHXoj8hvEqVNGH3+jM5k8xN+CZ5QLFGuV8T9XbKDlKUHj1KUWN5Peh59I0YhcNol+aM/kcy+Owe0R4f86Izg6T/GJSZkqyNcWc8JjNRBZlaIZ57o3E3xn/SZVZRXGrYqKLu7qnOdD4H0dKT0MRJe+twmlRmT3ETtzI1Kj9imgV/PTep9z5VM73XCDll0e3EeLdwTYM4XdZkDDCA9X/WSDrQrak5BCu6oQXrT8YNOsvRtQHrXNygrkeG4Qg6mD9SgZ/7MVDEpMlUW/t487pcoRU2twyIDdjaEVUFQaxnPJwxHVPKUQNIlS9IFzqOC8h1Sq2QCfB9GyNU=~-1~-1~-1; NoCookie=true; bm_sz=FE64725E5E26FDBCA342613CFC1420F4~YAAQS1LNF5/vF8KPAQAAKpkx6xgO8odG66Dkgy3aX+lViLasprclCHL4qV/mqQX2I3A7g0l0gOxMHjvfNx5CPgruJ49rwcMugPSQs4pUTIemAU0zfcjs5tKxQ6bCtO0e4lMnxOlYvA8AIQmR+j2X0lA0htu2I1q7lzltyX+7hLhndopYMXR2tNPZ/W7okVB7O9H1YlF7I7rD3/iq2LuHns3/dmE4+Nk4kTQqrt3gNnZZReEePlmMYHNTSvMcxKOzUf+OJ5qi6iAMuYBGMSSFmHi82I+kBbvkLMfBtSFR0C3luWXNbbo27zD6G+MuWA+p7rr8QcqL5/zMlx9q3UFI5dDJ2GEcLAtfaGo5FYyy3TGuNqHPj2jC5DQdSf6u3zA/m0LP75FnYmptL2XWfgUbg2EHCxAiPrriYc+6wPK9a9qZ3L8DjecS2HR+~3159602~3421240; _ga_TV3LS85R98=GS1.1.1717636576.4.1.1717637857.0.0.0; fs_uid=#o-1TY56E-na1#d8b77c66-f992-4069-94c3-d526a2bb84e3:6631b551-cf9a-4cbb-95f5-328d7c74914b:1717636576924::6#/1749010250; uws_session=%7B%22start%22%3A1717636576506%2C%22count%22%3A6%2C%22referrer%22%3A%22%22%7D%7Csession_timeout; uws_visitor=%7B%22vid%22%3A%22171747411554946781%22%2C%22start%22%3A1717474115549%2C%22count%22%3A65%7D%7C1725413860328; _ga=GA1.2.1834444413.1717474114; forterToken=80ba6a5d5b9d4f00af1e448402fbaa6f_1717637850584__UDF43-mnf-anf_13ck'
    }
df = pd.read_excel('links.xlsx')
links = df['ln']

for url in links:

    time.sleep(random.uniform(3,5))
    response = requests.get(url=url,headers=headers).text
    print(url)
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






