import json

import requests
url = 'https://www.autozone.com/batteries-starting-and-charging/starter/p/duralast-starter-19082/265620_0_0?rrec=true'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    ,'Cookie':'AZ_APP_BANNER_SHOWN=true; mt.v=5.808966057.1716899646541; JSESSIONID=s_y_MYu3OOnY7EMbrGslIm-kFHgK7t2Wd8jy86-y3VLqPjPSkJuu!1921469690; WWW-WS-ROUTE=ffffffff09c20e0645525d5f4f58455e445a4a421730; preferedstore=9801; preferredStoreId=9801; eCookieId=24389340-020b-467c-92bb-e643b49f5dd8; TLTSID=8058ae68afbc16549d0100e0ed6ab7dd; TLTUID=8058ae68afbc16549d0100e0ed6ab7dd; sbsd_ss=ab8e18ef4e; akacd_default=2147483647~rv=19~id=aa5de51f66c30911e891121bde1e27cb; az_bt_al=1b5ced86017ed7e0e59a02e62775c8fd; _pxhd=4bc9796076739bff294c913eb7d4d946c26edf813523a51c89071c42e617238a:928317a5-1cee-11ef-a013-3b9d230201bf; _pxdc=0; bm_sz=A0BD35C1A16DB8BE5CBDBD18E21DFC94~YAAQO/AgFy47FamPAQAAYJQxvxciBj27pDQqoT/zEWpehEfTW24y3cMl5UxP89XgdzBRuAGKNe33KKxWUGP95mexrPioYnwXCO1W5LNBRatXID3sGroSpViHoly0tHWWR5QJp+HnBBpX/7MYQMKFW0Wg8W3YNpY+FXbsUTebybHQJA9WQt+vkTMuoRark59ikhbHlmVdJr3bpa/4Mfm4kvxBIlk4k/z4B19i7Ohi4sgVuyiflGjbQ+iqXi2D5caqBGv0TRedMczAWCDADEGmKZ9YNW+DxGw1+qhpOizBhg0RvIMkGq2ryMHe/zrNpcc0mLiciX49n1C07fwpBdAy0OxlBYILdTvLr7JDsrhqGvDWtKEoq8smKrPK0/pkE+lTCfvhNKoVRozhdQcOmpNKDw==~4536629~3556933; profileId=274387579750; rewardsId=; RES_TRACKINGID=848601592390231; userVehicleCount=0; cartProductPartIds=; cartProductSkus=; cartProductTitles=; cartProductVendors=; cartUnitPrice=; cartCorePrice=; cartDiscountPriceList=; prevUrlRouteValue=%2Fbatteries-starting-and-charging%2Fstarter%2Fp%2Fduralast-starter-19615%2F776863_0_0%3FsearchText%3DStarter%2Bfor%2BCivic; redirect_url=%2Fbatteries-starting-and-charging%2Fstarter%2Fp%2Fduralast-starter-19615%2F776863_0_0%3FsearchText%3DStarter%2Bfor%2BCivic; ak_bmsc=2E3041AE80E0ED1920880C3640953025~000000000000000000000000000000~YAAQO/AgFwk9FamPAQAAhKQxvxc4bsY5b/gO39Cvnl23mxL1n18TEVxki3caq+wh2F9jrGPwPVGqYaDO/fU6lOxawbO74ZsVmqH2XwdCUMsanCKIlfwyTVT0uew/k9l4t+3zHKmUXywwwP+XW+KvDslEn+vqqM00p49BDd/146wmTH9HAF5TDih72I7cxiPgap+cpnApQraKSPUExXXSd/G7IsMYMo3cLUjSv7y/NfHVQUg6C4xSpwBWZV4y9SLnjHsf8O+Qv3A45o/tUcZqhy1ht9JXitU1f35/Ao1j79SpHbYR6+J6IhXrFC7WnhptOLf7tKouA8DoPF7FJs4ngvz3ft29zloewlLDs4/NCo1a7AfdKDf4ToAMsm/stJ3ZHnpCFJTyA6wvV114i2WGHX2g6E9clWATHCJ6IW58oXYasdbCSl1WO+82rzuuPzr9wxAjup+2TbCi; bm_sv=A54D268DE9A51275F0D68361FA3522BA~YAAQO/AgFwo9FamPAQAAhKQxvxcmH3NH02R6VQLRGghqCF/88DB0G4oz8Yo2AuYx9Cyn1Z1xyzktNAIHRW+W/1KPUnS4sncTDpo+qBRJMWyeu6VNWRhxDh48as9kcjxNEVYWkYVoFaKhE8doNXdzddfZwUE54decxr+C7VZ948RFOpyvZNCtS0QA4jovDGt5uPohck62vs0Py8LFT+IUpiCo7B6DfQ3GJXSmvDVtbWUT/A0Ig/t3GupThvRBjcSofBM=~1; az_bt_cl=hPp0YAbH2l1Jzlm4TTBcIYQrYKyYqoPKhRRaK0nv9fFl6JkSJa2cuhkbSrJT5rSQ; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+28+2024+20%3A34%3A13+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=71bccfce-b3ff-4e43-8487-22057b2d7f94&interactionCount=0&landingPath=https%3A%2F%2Fwww.autozone.com%2Fbatteries-starting-and-charging%2Fstarter%2Fp%2Fduralast-starter-19615%2F776863_0_0%3FsearchText%3DStarter+for+Civic&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1; BVBRANDID=7d4ea9c3-d8fa-434e-b4e6-fada95400f3b; BVBRANDSID=b7fed924-5fd8-435e-871b-a5b76f65f926; sbsd=shkn1C+aPDg+5tCL5Rp35m7c3wGGFj1o/MPT+Pecx7JcB6gqZgo+8dcrTdQEj+na3rllz76IT6l9aipmC6ewkC8mXv1O3MuEFY+qD0bqHjEhl8q7u0ZJe6HTOAfYNe8i87m0o6Q7SfZTWx+qGgUo9pR6TsAhYnZNxwgI+kVIOS8dVsbybwZ0PJyBF3hNS/ubG; _abck=47571064539E06B51520B3C2FAB7138D~-1~YAAQO/AgF3FSFamPAQAAgUMyvwt7+sL5cxdWpAyHaKcyYESsBdZTK3ZsPG7ap/N6DBXIVozC3WZ7m83LjkzOr3dn7hES+F1aXjcDW9WuJmEbJ0HcX+Gs8IOvDJ+Low7ZuXM+hn0nhRur+x09AGIFXsmmRJw8lfSZ2Mg+FLYJasFdYinffEnvvZfrKnl09QwOLgwzGqYGJisAmLFnPJz7/8Dn76QwnFHlEkdvXfVlfg1FYEwTAicIxcJUQVuEU05qzADrCokiWq0UaF7XHIsZde9G4SITuXS3ML8Wf+YeIYATi96rEfjLiYh0+DwL9RphZum2tDLDB3B9O4g5dLEFDaAUs68LZSzZh0auasXFwPijhzP7QFYXa0dy2567RZLfMe5j5kRHQdRNP/wQ~-1~||0||~-1'
}

response = requests.get(url=url,headers=headers).text
print(response)

# # 定义参数字典
# params = {
#     "country": "USA",
#     "customerType": "B2C",
#     "salesChannel": "ECOMM",
#     "preview": "false",
#     "vehicleMake": "Honda",
#     "vehicleModel": "Accord EX",
#     "vehicleYear": "2018",
#     "lineCode": "WWD",
#     "partNumber": "19082"
# }
#
#
# # 基础URL
# base_url = "https://www.autozone.com/external/product-discovery/product/v1/products/776863/fitments"
#
# # 使用urllib.parse.urlencode来编码参数
# import urllib.parse
# query_string = urllib.parse.urlencode(params)
#
# # 拼接完整的URL
# full_url = f"{base_url}?{query_string}"
#
# # 打印结果
# print(full_url)
# response = requests.get(url=full_url, headers=headers).text
# print(response)
# js_data = json.loads(response)
# for i in range(len(js_data)):
#     print(js_data[i]['name'])












