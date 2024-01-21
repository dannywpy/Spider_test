import requests
from bs4 import BeautifulSoup
headers = {
    'Cookie':'t=565d10e404f8b1db7e1a79c8b2e9e54e; thw=cn; cna=qUnWHXGzFXoCAXJdCt77yOOJ; tracknick=%5Cu968F%5Cu4FBF%5Cu4F60%5Cu54AF2; mtop_partitioned_detect=1; _m_h5_tk=27cdcfc76aa15aee78ba2a42112179ea_1708338753625; _m_h5_tk_enc=c3c8bb8bfe8acad936b4a803dc13c675; cookie2=190ab6adf95e7b68887dfec3324bc624; _tb_token_=e0e7e1e75e713; _samesite_flag_=true; 3PcFlag=1708329761838; xlly_s=1; sgcookie=E100yRO0u1vFXwD36lggBLpDtar4JRDAtUbFg%2FwsvGL38Jr2ewziiJu5wwTNHALo2h7KvgHwLDCA5i7XzUJde0jAAQ%2BiOiF12w998j85mN2as%2FrSyqMA0yF8GYa4dmuD21IN; unb=2310259824; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&id2=UUtKfwFTaQo87Q%3D%3D&nk2=qE4gCfk3XdFo&vt3=F8dD3eu48qAuuxgm04o%3D; csg=44c92fe0; lgc=%5Cu968F%5Cu4FBF%5Cu4F60%5Cu54AF2; cancelledSubSites=empty; cookie17=UUtKfwFTaQo87Q%3D%3D; dnk=%5Cu968F%5Cu4FBF%5Cu4F60%5Cu54AF2; skt=689f4db571ab89d4; existShop=MTcwODMyOTc3MQ%3D%3D; uc4=nk4=0%40qnWNzY5qZCmaIUlB72uIJ9xyfPk%3D&id4=0%40U2lwLtK1FPtFpbbXRDPuTOmp04EW; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=243; _nk_=%5Cu968F%5Cu4FBF%5Cu4F60%5Cu54AF2; cookie1=AHnSRFnBJFfMB4ypX3uoMB88IWvW%2BzLXECUKZmU5gsk%3D; mt=ci=145_1; uc1=cookie21=URm48syIYB3rzvI4Dim4&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&pas=0&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie14=UoYenb4eonKnPw%3D%3D&existShop=false; x5sec=7b22733b32223a2234633662653834346362373235343032222c22617365727665723b33223a22307c43494b5a7a4b3447454b43636a2b76352f2f2f2f2f7745614444497a4d5441794e546b344d6a51374d54444f324b4c5a2f662f2f2f2f3842227d; pnm_cku822=140%23A%2FSxGzRjzzZJrQo2%2BbGuK6srmSyIqWgmUv9EJgWaRxVEYtsJR0MSyAbmk3nNrfra3bgSlp1zzq0bT4tiXzzxYKNc7ph%2Fzzrb22U3l61xRDrbV25etFzx2oQ%2BmtII1wba7X53zpy0KhYL1ceR9TTVYGMaX8%2FqZj9qwGayGAQceQYzYF3mCTsEFD9Bpnk%2FqYIIlXyEdxMW1%2F228Da%2BhdVJNGBrQ9YurnAJBeC7oBkyqvrNArbxFRuCSpCVizP68%2FnXxAY7vaszQd5ppbiiaF1cK7i7uwUJgcssjGv37za%2F5%2Biz5Ak9CPQsrAaUPMQ1vWQmKGOSPCpqROIvMFmFbTgSLh4G9A0B2wAqr3MyRQHA2UXPzZ1Ilr%2BoKg8xNVOynxXEZ2te3C1IIsC4oRvG8IQUdt598XY6z7%2FnHP1jkOhPnDMq7bma9UhKcr8q2EVXrl65wQrEbYFPDetwL5tJagG2zThaV%2FOX%2BC6h2hadXHiodEhgPKmAr8NZMN%2FoON6Avgd1WUydvhq8gTUujDtuGerGlYheOOSJtmpzQuurH4lLlvOE70NW%2Fod0LxtjtwNExioRMm638xN0vGv1h1MjPMbp4z%3D%3D; isg=BE5OEaRhp2pYjhPS87-OZhTJnyQQzxLJ-wU7aHiXvNEM2-414FoD2M2ZFwe3Qwrh; tfstk=ehHHm3tKkXPQtRWjX2eBBToKZ1OTAww7R4B8y8Uy_Pz1p4eLeOSa2u4zzTrFQfmjryKWOJhgrVug89KBO7zoRP3ReDHo1TmjVvKQeHwIA8wykEpYrDiQFRlmXYpxY8iZvELvHddFb8YHkXUsrYsnK_JK4ZkXxJ4cmNYH5IJbTroU8DnKQu7YuDzGUTz3xWAtYPXPUAsy215VlDB7b3HNN_NUfl4xyi5TMFBeSn-MjsG7TlZ0khxGN_NUfl4vjhfXPWr_mrC..',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Url-Hash':'http://shop581100855.taobao.com/search.htm'

}
url = 'https://shop581100855.taobao.com/search.htm?spm=a1z10.3-c.w4002-17866270723.66.423658a72FCpby&_ksTS=1708331664390_93&callback=jsonp94&input_charset=gbk&mid=w-17866270723-0&wid=17866270723&path=%2Fsearch.htm&search=y&orderType=price_asc&pageNo=1#anchor'
response = requests.get(url,headers=headers,timeout=(3,3)).text
data = response.replace("last", "")
# soup = BeautifulSoup(response.text, 'html.parser')
# names = soup.select()
# img_link = soup.select('#J_ShopSearchResult > div > div.shop-hesper-bd.grid > div:nth-child(2) > dl:nth-child(1) > dt > a > img')
print(data)



























