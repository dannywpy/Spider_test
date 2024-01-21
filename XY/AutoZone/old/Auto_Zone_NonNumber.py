import csv
import json
import re
import threading
import time
import random
from fake_useragent import UserAgent
import pandas as pd
import requests
# 使用urllib.parse.urlencode来编码参数
import urllib.parse
ua = UserAgent()
headers = {
    'User-Agent': ua.random
    ,'Cookie':'akacd_default=2147483647~rv=98~id=def58697d268ec07137473690e99cf8e; _pxhd=7e143722cc7891087b2e1b69a3ffb7a352f8397e08fe2a7379bee98008d6cc55:d1db8187-1dbd-11ef-b214-9ec171142a40; mt.v=5.1008387416.1717229160618; preferedstore=9801; eCookieId=c8cfce7b-c4e2-4a59-aadf-efa456be6d57; RES_TRACKINGID=728702132442521; BVBRANDID=c484c3fb-3aeb-4a20-9ad7-e694871544fa; OptanonAlertBoxClosed=2024-06-02T13:43:08.916Z; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Jun+02+2024+21%3A43%3A09+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=71bccfce-b3ff-4e43-8487-22057b2d7f94&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=JP%3B; _abck=47571064539E06B51520B3C2FAB7138D~0~YAAQLvAgFxRky7+PAQAAp/oE4wylKeXPmGlLiyaweDfuNbtYITW6ip8FZcMEgRkuCEGH/G9tAiiTEKdEJhniB4ND5UlrWLYVJM3bjtsDPg+aJmnXePDZCaHdWSL2BRq3xBbd19Ax2aeraCXrTxpFObNdevzUfBuv/LQndc5JED8nHhBtKQLBsNIz3oHwemQisYPpibjjpHdhjZY3DBxFK72zCp9K+zcMADBMZzmiBuZ04jdmW+1zZnW4a+OPTO5+OnlAZ0M5lsKmYcfH11ULTbmPQVQVFToFAQ3tt2s7em8ZYHbEu8Bfn0nUmQyUs1ZuCVTM8k/Pqn+rlsVOKpQq6oTjNkq9IfQmTOusCg++EmRKIvDMR4cW4Y3OHnxKcfIazB7d9F9B9SJAWr78CJp3dWtRZxdDWMx1yj8=~-1~-1~-1; ak_bmsc=1F082F7990673583AD36ABAF32749A02~000000000000000000000000000000~YAAQLvAgFxVky7+PAQAAp/oE4xj2Qsacnpz1FcCxy2t71+sSiJ+LwNyxfn4YzPG1cXSZbotojmr8ROJKukS0YbbEAI+m+rBXr6r2Plg5vT+vxkm+u4zkQvtGIQNoHPEn7jfVpEPBTp/kNN97IH3zNgw0swZY3npxVAFwS1HjDQExbjGIapMocWDGgtkjC/2x9OraWIprgRaYMhgBdiilZBLZWw3CM2ngeX5ZgSoJlJHRvKFQsOkg1W0qF2UsbNJKniCdXbkDDX1vfJG35a4nUIIl+Sshb7cGK4dHk6SPJwD2MMw1JyXk1oicv5QdbKru2oeakYlV7ootb/zH36/++vnhIF8qH0Ur/cvqd0G/ElzSNCSUYdaSojl+1RUkni8KKvDBWcTVcmv3QSUk/Q==; az_bt_cl=hPp0YAbH2l1Jzlm4TTBcIa5CNxygy2C+Ftqn9Nq7zmRKi3yoHZ9qpbcZgwN21z0W; az_bt_al=da54bf7a5ccab3adef4768f1da96b7bb; TLTSID=8091e0d0afbc16549e0400e0ed6ab7dd; TLTUID=8091e0d0afbc16549e0400e0ed6ab7dd; sbsd_ss=ab8e18ef4e; _pxdc=0; sbsd=s+PPEW1byU4dBgRdjrSs82wtXLgEeGvLZS2JUaeatjlcTW86d0GBNWpiI7xfEMbNK6p+n9PnI0WGOQGtLk1mYiExLj3PBXFoP18X67bvq5Ia2OVWm2eL1IYuG90Wbf3xg5H+K6cgX5jtx7ry95x+L/c9sBbRMHwY+TRV3pBvfaeQN5SUSuDKbXaOgeOi6IQmL; bm_sv=4189AD350E078491B64396ADB3E83E94~YAAQV6fLF0qY+6+PAQAAYg9s4xjx4xgHMuoehx302wWR7ePk2q44hhdT28XAiRLxuO5Amq09L4FyM0BYdYZAeAIL2Veiz4hTrs6VIQ/52/414aS9AQoDpd0XM+/esjYgUEHQVLOKdZrVrKjT3xc8/crAvQO+Dn1Y7SHXLp1CBBrbPcDqOrKEw/gsxB/v7UPBTtzHDGQO2wc4rN7CZV3Rmv0RRvjRGhvnZm5HmptzR1TXd4DRyOGwIy7H7vYzCk+CcGU=~1; bm_sz=5DD24103339D34DAE54213833109B91A~YAAQV6fLF0uY+6+PAQAAYg9s4xg+Cyh0A4TriaPODuAKJaHuEsJLmzO0cmduGpjaA/g4ax240lbe3xl9kj7t3xyqwEfdn/TwIt9h6oK+hvZ/0nNoGKJPAGFz/PicM0Gpt4x2alFDz8l5Bop4dzq/D7TRXsyj2wIKRQrpVjR/l6YQ5HmeSPltsaneT7L3TrPmH6lTDvsAfgVRyKnc/ywxQyB8fss9nWnQirnRr6QPuONgNQz1GWVgHJ6yLOVIV06GNHzjRcDd374cIor21B4I8RT3kGpwVbZcnXRDHU8UI5uXRcCUPwq8K1Ng58gLMowMLTrhadvZ1F+Tzf0rzs9aVII7cWetD4G5HbkVcb8mbbr/G8l+QHfntqjubofET97dIFhCN0xL0Cf+3uap8T/dwh6enlSHK9oRDUYDPm6sjaCFRBiIUogE~4535090~3223618'
}

f = open('number_muilt_nonnumber.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['Part_Number', 'Make', 'Model', 'Year', 'details','link'])
csv_writer.writeheader()
# 假设第一个数字是part_number，第二个是SKU
sem=threading.Semaphore(10)
def muil(part_number,product_id):
    params = {
        "country": "USA",
        "customerType": "B2C",
        "salesChannel": "ECOMM",
        "preview": "false",
        "lineCode": 'DUR',
        "partNumber": part_number
    }

    # 基础URL
    base_url = f"https://www.autozone.com/external/product-discovery/product/v1/products/{product_id}/fitments"

    query_string = urllib.parse.urlencode(params)

    # 拼接完整的URL
    full_url = f"{base_url}?{query_string}"
    print(full_url)
    time.sleep(random.uniform(1,5))
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
        time.sleep(random.uniform(1, 3))
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
            time.sleep(random.uniform(0.8, 2))
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
                time.sleep(random.uniform(1, 2))
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
                        'details': vehicle3
                    }
                    csv_writer.writerow(dit)
if __name__ == '__main__':
    df = pd.read_excel('part.xlsx')
    part_numbers = df['part']
    product_ids = df['sku']
    threads = []
    for part_number, product_id in zip(part_numbers, product_ids):
        sem.acquire()
        t = threading.Thread(target=muil, args=(part_number, product_id))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f'===============================================================================All threads completed successfully.')


