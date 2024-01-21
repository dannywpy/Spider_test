import csv
import json
import random
import re
import threading
import time
from random import uniform

from fake_useragent import UserAgent

import pandas as pd
import requests
# 使用urllib.parse.urlencode来编码参数
import urllib.parse
ua = UserAgent()
headers = {
    'User-Agent': ua.random
    ,'Cookie':'mt.v=5.808966057.1716899646541; preferedstore=9801; eCookieId=24389340-020b-467c-92bb-e643b49f5dd8; akacd_default=2147483647~rv=19~id=aa5de51f66c30911e891121bde1e27cb; RES_TRACKINGID=848601592390231; BVBRANDID=7d4ea9c3-d8fa-434e-b4e6-fada95400f3b; _pxhd=5680b06f38bc28a1e209f64fb96990d07e2275c45904881b3ac939f3d3d01b59:ee2bb167-1cf3-11ef-a294-f6798ac0b123; _abck=47571064539E06B51520B3C2FAB7138D~0~YAAQhfw7Fz1TKryPAQAAgexn0gs4zXUdKDfgBu88LkLx3gM88pPZLw+EPP1wh/TKpuJ0uCz/ml5H6xzwHeC4nNGtCmyJ1xdM9uL+u04oirvxGWg1sLfqud7vXaCBmhZ03omzK+8FzOvjljv2K1ApnhFmXE8E5ybCyQKpFQQbmNYwzQzmONT79xUCypdPJhgk86yR8OgcF9uOV0VeNZd0Gg5AzljZ2DMlGd/y0QuhqTgoyTM9P63WLVqTAsHAL4AR/KBoCw8rUHr320eMABx8gTq3VCso9hXemDB31yrLWx69eqcl2hgUnC/yXDCS6hpRFGGEQEDxBckExeltKbNmn0F82q3M/lLj5moasvPvun/Cdwx71WUfwR9/JN0+JxXkhWfRJJDq8fZrJKa+dF3uT80/TLRMEMPwoT0=~-1~-1~-1; az_bt_cl=hPp0YAbH2l1Jzlm4TTBcIWvTT22HCXr6Vzo7/XahoViHKEVf2UHDL/PavxxcQlBT; az_bt_al=5d62546fedcc518fae13f6fdabcbea1f; AZ_APP_BANNER_SHOWN=true; preferredStoreId=9801; TLTSID=83474da7afbc16549d0100e0ed6ab7dd; TLTUID=83474da7afbc16549d0100e0ed6ab7dd; _pxdc=0; rewardsId=; cartProductPartIds=; cartProductSkus=; cartProductTitles=; cartProductVendors=; cartUnitPrice=; cartCorePrice=; cartDiscountPriceList=; prevUrlRouteValue=%2Fbatteries-starting-and-charging%2Fstarter%2Fp%2Facdelco-starter-12627135%2F1183299_0_0; redirect_url=%2Fbatteries-starting-and-charging%2Fstarter%2Fp%2Facdelco-starter-12627135%2F1183299_0_0; JSESSIONID=NGzSuJfxLW-RXK6gY9W2OvlmMEQXOHWGDV3ePZlAfXM3nFFC0dwI!1018208960; profileId=274657871560; userType=3; nddMarket=MEM%2C%20TN; nddHub=110; nddStore=6941; availableRewardBalance=0; preferredZipCode=38122; preferredVehicleYear=; preferredVehicleMake=; preferredVehicleModel=; preferredVehicleEngine=; preferredVehicleId=; userVehicleCount=0; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jun+01+2024+15%3A34%3A55+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=71bccfce-b3ff-4e43-8487-22057b2d7f94&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=JP%3B; OptanonAlertBoxClosed=2024-06-01T07:34:55.640Z; sbsd=sACS+12y4AS+JwA3fBqDY9JdDHu1ITQ/Fto7V+gj/sEiCtVkeiXmY5BL5zWMSctqgVJLGvS/u7xhuagUsmNZz7i0IyJFEg00YS0oNCk4+egAKUL/bv8cawqb5WQF7kEkwy08P4tQW0/JXROlhyvuh2zlM2BolLNqcFodNyO8PNKIBMLWYkEwlfXNEQ0qU+hA1'
}

f = open('number_muilt.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['Part_Number', 'Make', 'Model', 'Year', 'details','link'])
csv_writer.writeheader()
sem=threading.Semaphore(10)
class Product:
    def __init__(self, part_number, product_id):
        self.part_number = part_number
        self.product_id = product_id

    def __repr__(self):
        return f"Product(part_number='{self.part_number}', product_id='{self.product_id}')"


def extract_numbers_from_url(url):
    # 编写一个正则表达式，用于匹配URL中的数字
    pattern = r'\d+'

    # 使用re.findall()查找所有匹配的数字
    numbers = re.findall(pattern, url)

    return numbers

def Auto(url):
# 需要修改的网址，纯数字的
# resp = requests.get(url=url,headers=headers).text
# 提取数字
    numbers = extract_numbers_from_url(url)

    # 假设第一个数字是part_number，第二个是product_id
    if len(numbers) >= 2:
        part_number = numbers[0]
        product_id = numbers[1]
        print('1')


        # 创建Product对象
        product = Product(part_number, product_id)

        # 打印Product对象
        print(part_number, product_id)


        if part_number.isdigit():

            params = {
                "country": "USA",
                "customerType": "B2C",
                "salesChannel": "ECOMM",
                "preview": "false",
                "lineCode": 'WWD',
                "partNumber": part_number
            }

            # 基础URL
            base_url = f"https://www.autozone.com/external/product-discovery/product/v1/products/{product_id}/fitments"
            time.sleep(random.uniform(1, 3))
            query_string = urllib.parse.urlencode(params)

            # 拼接完整的URL
            full_url = f"{base_url}?{query_string}"
            print(full_url)
            time.sleep(0.1)
            response = requests.get(url=full_url, headers=headers).text
            print(response)
            js_data = json.loads(response)
            for i in range(len(js_data)):
                vehicle = js_data[i]['name']
                print(vehicle)



                params1 = {
                    "country": "USA",
                    "customerType": "B2C",
                    "salesChannel": "ECOMM",
                    'vehicleMake': vehicle,
                    "preview": "false",
                    "lineCode": 'WWD',
                    "partNumber": part_number
                }

                base_url = f"https://www.autozone.com/external/product-discovery/product/v1/products/{product_id}/fitments"
                query_string = urllib.parse.urlencode(params1)

                # 拼接完整的URL
                full_url1 = f"{base_url}?{query_string}"
                print(full_url1)
                time.sleep(random.uniform(0.5, 2))
                response1 = requests.get(url=full_url1, headers=headers).text
                js_data1 = json.loads(response1)
                for a in range(len(js_data1)):
                    vehicle1 = js_data1[a]['name']
                    print(vehicle1)


                    params2 = {
                        "country": "USA",
                        "customerType": "B2C",
                        "salesChannel": "ECOMM",
                        'vehicleMake': vehicle,
                        'vehicleModel': vehicle1,
                        "preview": "false",
                        "lineCode": 'WWD',
                        "partNumber": part_number
                    }

                    base_url = f"https://www.autozone.com/external/product-discovery/product/v1/products/{product_id}/fitments"
                    query_string = urllib.parse.urlencode(params2)

                    # 拼接完整的URL
                    full_url2 = f"{base_url}?{query_string}"
                    # print(full_url2)
                    time.sleep(random.uniform(0.5, 1))
                    response2 = requests.get(url=full_url2, headers=headers).text
                    js_data2 = json.loads(response2)
                    for a in range(len(js_data2)):
                        vehicle2 = js_data2[a]['name']
                        print(vehicle2)


                        params3 = {
                            "country": "USA",
                            "customerType": "B2C",
                            "salesChannel": "ECOMM",
                            'vehicleMake': vehicle,
                            'vehicleModel': vehicle1,
                            'vehicleYear': vehicle2,
                            "preview": "false",
                            "lineCode": 'WWD',
                            "partNumber": part_number
                        }

                        base_url = f"https://www.autozone.com/external/product-discovery/product/v1/products/{product_id}/fitments"
                        query_string = urllib.parse.urlencode(params3)

                        # 拼接完整的URL
                        full_url3 = f"{base_url}?{query_string}"
                        # print(full_url2)
                        time.sleep(random.uniform(0.5, 2))
                        response3 = requests.get(url=full_url3, headers=headers).text
                        js_data3 = json.loads(response3)
                        for a in range(len(js_data3)):
                            vehicle3 = js_data3[a]['name']
                            year = vehicle2
                            print(vehicle3)
                            dit = {

                                'Part_Number': part_number,
                                'Make': vehicle,
                                'Model': vehicle1,
                                'Year': vehicle2,
                                'details': vehicle3,
                                'link':full_url3
                            }
                            csv_writer.writerow(dit)

                        print(f'succesfully   ====================================={url}')
if __name__ == '__main__':
    df = pd.read_excel('input_file.xlsx')
    column_name = 'ln'
    links = df[column_name]

    threads = []
    for url in links:
        sem.acquire()
        t = threading.Thread(target=Auto, args=(url,))
        t.start()
    print(f'succesfully   =================={url}')







