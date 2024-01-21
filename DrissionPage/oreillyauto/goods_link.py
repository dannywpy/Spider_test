import csv
import time

import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
f = open('oreillyauto第一页商品链接.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['part','line','link','select'])
csv_writer.writeheader()
ua = UserAgent()
df = pd.read_excel('links.xlsx')
urls = df['ln']
headers = {
    'User-Agent': ua.random
    ,'Cookie':'trcksesh=bd7ce385-e9f4-4b3d-a596-603e9cba866c; OSESSIONID="68b1fa1bfb018b84"; dtCookie=v_4_srv_4_sn_9F306E64A40C887FF2DD9CBF005474C8_perc_18607_ol_1_app-3A200c4c21b0fea6c6_0; AKA_A2=A; akacd_ost-prod-lb-2=1717550457~rv=54~id=140263145a5c4d0f369b898fd3afb21d; _abck=CF755594DDF57659D5FFC58514992E49~0~YAAQS1LNFw+jNcGPAQAA4gVp4wx12CnNgc1ITy1coDx9Xef01Eia5R0kyno1H/QYqQLfR78pYmgKP0ZLIc3t6VuzKXB5JwPk7ZKqdGHZzFFvTcnB84e4tsPyHmVx5qzioG8bKmLi0oKoch2R0KGAEdtR7oR6+o2xuWSxHaaQNVx+d3Cv6QnSIPp64d1qh/4qHjqkUY6VaNEjpUhJhyqYW6jsogWJmUiLqm09j3mPuNAHBZEcVi4C3DgP/7gx1it5eh2jQ16lBrhJF7Bk+7b3yp3c8qb2XbApE+AiDqHENz/Rik6B7PJk680XWM3T+Qv1L9i7rstMsQTmmUt1vfUbh+j4SuQWG1CiPO0SUXK8j33v/X0mGBqvjffcbo9GSmOlqvBRyAtYlptV1Antprdwgr2A5CBD18yL+1R4StM=~-1~||0||~-1; ga_session=6c32a84d-64c2-4794-9bde-b6499d6e8423; uws_storage=%22cookie%22; __wid=164969602; __pdst=4bc079921c39473f943b7ccfb242a57a; uws_prop_8swyp7jh=%22N%2FA%22%7Csession_timeout; uws_prop_5lcxgghj=%22N%2FA%22%7Csession_timeout; uws_prop_q8ub7x2l=%22N%2FA%22%7Csession_timeout; uws_prop_vn35otqo=%22N%2FA%22%7Csession_timeout; uws_prop_8jo1u2t0=%226c32a84d-64c2-4794-9bde-b6499d6e8423%22%7Csession_timeout; uws_rate_comparators=%7B%22global%22%3A17747386%7D%7Csession_timeout; NoCookie=true; _fbp=fb.1.1717507284190.249225726405179591; _gid=GA1.2.1457245848.1717507285; BVImplmain_site=14810; LPVID=ljOGQzOWQxZWZhZTg1YWU3; LPSID-16349016=kX4xC7cuRjCxdzl-S77VHg; uws_recording=%7B%22status%22%3A%22recording%22%2C%22conditional%22%3Atrue%2C%22requestActivation%22%3Afalse%2C%22recordingType%22%3Anull%7D%7Csession_timeout; JSESSIONID=E2FF2D80919496ADF3A1EF06772DBCAB-n1; ActiveID=908S-C7LS-VHVW-B6QR-ZPPJ-1PFR-LIBM-TOLH; cust_id="qL+g06dzW8fCd/s9Br1fjf9QR9+xpFbjyhUx+Ntnz0I="; bm_mi=B5711EDC9C859DD0AB6B355483B397E6~YAAQpl7WF2bLrr2PAQAAe+Nr4xg8v4G1Q7Whp59dXowOu85j6vMpt/bFcwNedPYofcwkui1XkfQJa5S8nmHGCc1xDf7W8phsUnAMi3BGPJNwEv0obgFlJNpfgwHt1NwgBJzEzNLpO22dPlWa8a0Ezkj9NqzLWoIK6lLyrnQouz7VmC4giR//4L92JerdFaanLMjjMa32hdA3tGXnCse4r0s88BRQbCq852KevNtZBv/04ntfCrErhx0FkuqMs4Yt4VDMSukkGCQBM8j/pszoJOJQqcLFalG60bT4F0QDscl4TzDcTXKMofv2i8B5k6YhXBAUV+QeB/sl5yhwYDom6AkhN/Yj3ZITmCsoWdaKREgI4QXAMUbPdCrujOtjqO3pO46mYPYsAJ3qbVQ60cLfs9ILgYzyD7otXYPGyoJDfaQexUXE+9v27cL7iDsLLsEBJOlYi9aoDU2NDqUVLBNc9/b7~1; selectedStoreId=5545; lat=39.392534; lng=-123.348256; ak_bmsc=55814EF7ED7B937B3BCC04640B933207~000000000000000000000000000000~YAAQpl7WF7PNrr2PAQAAGPJr4xhXan9p7IeHu38qoW3M6sBUTBSqPQWJDg33vXuUplgmjEkOCSkW8C35JNbh6qg7lcXLd1wjp4bNw2RN+kJfL988y191MKL7A5c+o6Wq7Cvp25W4BoKNVH6/ewHBK+pHqRHotPP32UOY1/09bZ9iPCDmwfi2eQ2kCT6HNmYV0cazj2S6OGQaUloNb++K2Xb3QGEu/oUJMYgs7dfpqbBbc8xyMoNSGN5xdUNfhyLcyiPcUw68gMRjTbBPjRtfesPXiLHQfC1+AMyyr6DiIqIF+giNOGylgnsOpFClyoXZPTBcJTNGTvYtfUnl5EDOy/VrV+h1Te/chn5BLiTF21qPr+jtTZEAWUOC1o/18T0iieGJxNpUgU2DJP4svuIeyx5/b2pBor4/38ziRzooPpA1WL922HtpWVWYbl7pboLvi5tpWwj2MtZ0vTVgbD31YyoYpJURZnS00g1TR5ZeQAffSDh3pIjlBixsjvse14jT9V6dRORh/86oR9aRQ3HyjJJfTmDTfpHavIfR0nX8cVh9Ex04XMNYUO1TmxVElHrj7AfFk7eYJ9P6ZuBU0hHDE4lRX+EpaJnyyhfWIuTC6UxZPO6rjKUUU5XpX2cj1q8=; uws_prop_w71w8mxp=%225545%7C1590%20S%20Main%20St%7CWillits%7CCA%22%7Csession_timeout; truyoConsent={"consumerCookieId":"334f1878-8484-476d-bb9e-da18b446713d","displayCookieBar":"true","flag":1}; EPCRVP="USL-N612453A,dad3c6651e74|USL-N612617A,dad3c6651e74"; uws_invite_shown=true%7Csession_timeout; uws_story_Orellyauto_Browse=%7B%22done%22%3Afalse%2C%22stopped%22%3Atrue%7D%7C1720099915113; trcksesh=8758d71c-2b63-469d-8b81-713557c17e0e; uws_session=%7B%22start%22%3A1717507283948%2C%22count%22%3A33%2C%22referrer%22%3A%22%22%7D%7Csession_timeout; uws_visitor=%7B%22vid%22%3A%22171750728394821536%22%2C%22start%22%3A1717507283948%2C%22count%22%3A33%7D%7C1725286558998; fs_lua=1.1717510559071; fs_uid=#o-1TY56E-na1#247ac87c-6514-4674-90ef-5871c9d7088e:b4f4fb1b-3573-4e3e-a4eb-91cf0f9f7245:1717507286525::34#/1749043353; _gat_UA-1862090-1=1; bm_sz=116C9DE8B606AE180837819502923AC3~YAAQlvTVF+5REamPAQAAGyyf4xgmRFLzXGotFSWUTdWnqXzsh8LXMFmCpfHq/Mne2Lt3fwKzWKY3/yrHVUYSO0r2/pSJwEnZghAH4o+6xQmCZiNPDNmRmSqFliukk++VTtiibD45jCu/BumlSEavsj4O/NwVTq/EG2jMSmIcXHhOFDgHlduccoM+D5wBNGl5zNErGgC/EDImL9oO5U2i7/RRj5tp0kLVWA2f3UpvouYhyUDrMFvBGVAe8bD4jicZL2haQS9zuAJ8iyV7ZrJ5YbD+a/KcuaUMdE2PdXFbQCX5JnnVI3VTirL2KLKVEeK+rb2v3mlUGDwcxHToMKyjRk79VceqzPcg2gwtbQNa/jnT0S0edakDr3KkmnbcS+YuImk0cFND9UbUNMlWhmHqdfZYL/4NbtnW60EJUIR3w5H3sHvNBsmHwU7zfE2O/lj4zZ4kvVcORPLPCehRuAXPhCoI46MX+iEWbq8UULcvFq+LyMPhYZEe7A2NXztMHOm9PcojK6jQtkwzr/SlWHtrx2hpQML6AiMjaGsANGgYsDBU~4276790~3162437; forterToken=e52ece034bed405b863fa4a29e77f3fd_1717510811039_499_dUAL9_13ck; _ga=GA1.2.261699399.1717507284; bm_sv=2239C47D13F33FDAF81A130C113DF793~YAAQlvTVFxlUEamPAQAA0jWf4xi4ji5xaJDqNfjbuEBDPiGtTOTf9d2sWTOkyL/YTP3ftu8Yq45P47haRczjmTEKdt2OKOynSgzce3Xa6M/6+T1uh2e7l+xJu1SG8dcds+IwubdtWSil5isx6oX1ExhaXwUbqcpM0NcOOIwLK+5EwjFHxYfxhZyAUTkHqlL5DIlmmKglKm3E6+ibHjUuQFoVexv8bK4q9HOZjuGfBSQRc6Z9DcLaHD3Y16N1jjNFIlRqdFa9fA==~1; _ga_TV3LS85R98=GS1.1.6c32a84d-64c2-4794-9bde-b6499d6e8423.1.1.1717510812.0.0.0; RT="z=1&dm=oreillyauto.com&si=61qur8dekh&ss=lx0fl9nh&sl=c&tt=gwv&obo=6&nu=442c2752e02ff2d3339c1cfa80f72c06&cl=20549&ld=2054m&r=91749d36e0c830de15a9a30b5f3835e4&ul=2054n"'
}
for url in urls:
    time.sleep(3)
    response = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    select = soup.find(class_='plp-refine_list--removable')
    parts = soup.find_all(class_='part-info__code js-ga-product-line-number')
    lines = soup.find_all(class_='part-info__code js-ga-product-line-code')
    links = soup.find_all(class_='js-product-link product__link')
    for part,line,link in zip(parts,lines,links):
        dit = {
            'part':part.text,
            'line':line.text,
            'link':link.get('href'),
            'select':select.text.strip()
        }
        csv_writer.writerow(dit)
    print(f'successfully ==========================={url}')