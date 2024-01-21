import requests
from fake_useragent import UserAgent
url = 'https://www.oreillyauto.com/product/compatible-makes'

data = {
        'lineCode': "ULT",
        'itemNumber': "R612249A"
        }
ua = UserAgent()
headers= {
    'User-Agent':ua.random,
'Cookie':'uws_storage=%22cookie%22; __wid=164969602; __pdst=4bc079921c39473f943b7ccfb242a57a; _fbp=fb.1.1717507284190.249225726405179591; _gid=GA1.2.1457245848.1717507285; LPVID=ljOGQzOWQxZWZhZTg1YWU3; selectedStoreId=5545; truyoConsent={"consumerCookieId":"334f1878-8484-476d-bb9e-da18b446713d","displayCookieBar":"true","flag":1}; uws_story_Orellyauto_Browse=%7B%22done%22%3Afalse%2C%22stopped%22%3Atrue%7D%7C1720099915113; RT="z=1&dm=oreillyauto.com&si=xl0b23zg6o&ss=lx0fl9nh&sl=d&tt=jw4&obo=6"; NoCookie=true; EPCRVP="ULT-R612249A,dad3c6651e74|ULT-R612302A,dad3c6651e74|WIL-71-25-18301,dad3c6651e74|ULT-R612268A,dad3c6651e74|USL-N612453A,dad3c6651e74|USL-N612617A,dad3c6651e74"; JSESSIONID=37BFA67A641E375337BC57ADAA449F7C-n1; ga_session=dd3accb4-fba0-4d19-b706-29d8ab2a9794; ActiveID=HOSE-HKGZ-6U2Y-LN8J-RBYH-5R3Z-09YH-ZGDK; cust_id="HDmTtI9kxjtdBK443kp9ExmB/5rx1frgPEgs+gFCVY0="; dtCookie=v_4_srv_4_sn_667B85AFCF0F49871DB146507A82384E_perc_23862_ol_1_app-3A200c4c21b0fea6c6_0; AKA_A2=A; akacd_ost-prod-lb-2=1717723487~rv=90~id=cfcaf0d4a36f9a6100869714f255f659; _abck=CF755594DDF57659D5FFC58514992E49~0~YAAQS1LNF5r+qMKPAQAAADC57Qy8kIdZBA5Pe4Gc3YEcOMPQap81HguG3M+FVkR4ddho1CVaIQmHVAPMLgRxbmmSdiqblHyK87LGlgT19iv2Ph1nE1WB4+Q4qK3B6OGDN3SDOO6nAiD7tqJHBYtBCb5wUYqPAGxzlbQ0JSf3USBfr6O1mVmurGnW1iZ4fJKUMg84b2kQ/Qv3wENEuAjF+jpzqs+OZXBi+FRoQMuFM+oNQF/R7rcaYfzdmwFkeuNLClDEbrF2xNz6Tztitx30cOwC7wee+UZkdXoFBm//Eyu1dr/C47MSD2JnDv96p3sjyfRpGx7CDzC2qr2ScdySQPCgI0PDlPLP8IoSTOtYu/Yc4bD0aimxKAOVKpOMzOyNEr9S+edEOYUy0vpDcUP6mDoLu5QkirBIehpTM5g=~-1~-1~-1; bm_sz=6E87F4A1EF4230DF5EE793EBDF537758~YAAQS1LNF53+qMKPAQAAADC57RgD5MXtocezjniG9OiDQL08mSmcshEdo02RF13U6OQpOb3T5VW03qKzUTIIM4kLqj5cnbai2lpSFWmpbrjc4d42jnFkCI9OKyad4manL9H1QFNwMIgEI02ZiYqm6rt36TRbs+jRkpXOIpbjY7Xikc3rRdGGfBvzarixyS3ebUgC5HBf4wMTO5zqbDzSlWf5wOB6Y6GM8tT+Ar9zrfiBsfz0+wrPAdkhSXtn+ExyxklFMy/Fz/biWe+Zuxrsq0MS7SD/Brv/KvaavSLbXVzQgmVElurLjlHlA/NBKgMgMpG3AmBFn6wO8+jjHEj5II18UtbUmnjHqi81p50CWkfVwq8OTdAxACTyPolZ6Kpz6H+z1XPPwXFkInK9ahVlZogTmQ==~3749445~4470580; bm_mi=CA3CC599CF181AD055D2835DAFD9F12F~YAAQS1LNF2MDqcKPAQAAlke57Rh65/9VyUtw2oYUnNzAi3uY+w/a48xZkewJSftaB1c5WA03jPKf7uvMVTxEuTBXWa77CurYjOoho5ZNWULtFHI+CJ+efQ1zjNPajqrSTvMaKAwSnC+Di/BbUJsWn9dbN2B0NQ0wnm6cpmGoPAqJ+kUL1Q77rKZrPiYdUF6k04NqocrABhxA7zyjpmHIoM+DRvRpxcq52PXQeTz3ykS1S01iBMpYPDrKD3DYptIXCFAZgW/DXpNd3BhhHdyIO3Mucp1HSZTK6sYjL4GJblfL3AGbTuQZEgPmSaeyibdRQqMqS1Th2vFDW9ARhTHBCHjZHxUGBoIEVsEI/w==~1; forterToken=e52ece034bed405b863fa4a29e77f3fd_1717680290554_454_UDF43_13ck; ak_bmsc=5BB7B28BEEDBEE48FB56283E7A26EE2C~000000000000000000000000000000~YAAQS1LNF4wEqcKPAQAA51K57RgfANkja47iu8z8HoFvopZlPOgbMmtrRKCrpnUBn4UjtqNvl1wPN4r4OFLdSAeLq1ZM9mZVOGKOpvjeEdDcUDvUHJpi/KmHHrfN+bCNZEOLCGtXoZcsSh9cd1QoAiNh9jxY8Utis3UFD5wdPca2N4OuDSn8z/GEbvDlwU80Tibegi9wt8kOg5vZ5Wr/2r/ry67mrqY7ZxyJ+F1CMSOL2PyvXVC4d/SJTHMt4qjQLZnRFiXxQ3rOuZHC/sJT4MT5qhcSLkaG2rhL8U8VeGwKOgn3SxEYSYSwk7iDGC6p1CuTX5OBd95/qgZ+31fpGk/hzIJgJgQLLNnB5dysHcITYAzgAVC+KJ8j+5Q/99ID/TrIRdkzpTii/wRJOAoG0VWlLSbyMWL42R0jYLtRZi/MAbpJdB770Nbw2jSpByE59ertqS4NHSwIcQwYwFU8it5Gie9zuVdvw+/6H5ulF3Sx7NLtupd+YIRf3xHuASE/SY57rXsMGO77lwRopj4=; BVImplmain_site=14810; fs_uid=#o-1TY56E-na1#247ac87c-6514-4674-90ef-5871c9d7088e:2738b9f9-afad-4b28-baee-0f18f9e9aa70:1717680300529::1#/1749043393; _ga=GA1.2.261699399.1717507284; uws_prop_8swyp7jh=%22N%2FA%22%7Csession_timeout; uws_prop_5lcxgghj=%22N%2FA%22%7Csession_timeout; uws_prop_q8ub7x2l=%22N%2FA%22%7Csession_timeout; uws_prop_vn35otqo=%22N%2FA%22%7Csession_timeout; uws_prop_8jo1u2t0=%22dd3accb4-fba0-4d19-b706-29d8ab2a9794%22%7Csession_timeout; uws_prop_w71w8mxp=%225545%7C1590%20S%20Main%20St%7CWillits%7CCA%22%7Csession_timeout; uws_session=%7B%22start%22%3A1717680303465%2C%22count%22%3A1%2C%22referrer%22%3A%22%22%7D%7Csession_timeout; uws_rate_comparators=%7B%22global%22%3A66343049%7D%7Csession_timeout; uws_visitor=%7B%22vid%22%3A%22171750728394821536%22%2C%22start%22%3A1717507283948%2C%22count%22%3A51%7D%7C1725456304717; uws_recording=%7B%22status%22%3A%22recording%22%2C%22conditional%22%3Atrue%2C%22requestActivation%22%3Afalse%2C%22recordingType%22%3Anull%7D%7Csession_timeout; LPSID-16349016=uPrwqHXaRpyCoSeWM7rjUQ; _ga_TV3LS85R98=GS1.1.1717680298.6.0.1717680364.0.0.0; bm_sv=C78D75F856F1AFAC91CAFE95158E3592~YAAQS1LNFyoqqcKPAQAAuGG67RjwtzNk9JMpTj/QYDo16gAY+Lo3ch4+P1p5550QXrXmOM099GRKiqN+7ecLm3NxXU/91+1gePrcVM8gpUIujLfOuRIFfDVMMtzduwRFjlobPSUGEfBHWg5CnZ0wQLeCUD3Kkw9P96grTBnoNr3bwqGTj7AgCEX5RynuXLwrIB5epe+mMCoUNAVY6g3K0Lzj0h1nKMTZUoYKF8lr+vD14bIG05J3cXrCvn/50xCOnZqYXCQ=~1; fs_lua=1.1717680894852'
,'Referer':'https://www.oreillyauto.com/detail/c/ultima/alternators---starters/starter/dad3c6651e74/ultima-starter-remanufactured/ost0/r612249a?pos=2',
    'Origin':'https://www.oreillyauto.com'
}

response = requests.post(url=url,data=data,headers=headers)
print(response)









