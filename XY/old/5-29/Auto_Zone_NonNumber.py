import csv
import json
import re
import threading
import time
import random

import pandas as pd
import requests
# 使用urllib.parse.urlencode来编码参数
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    ,'Cookie':'mt.v=5.808966057.1716899646541; preferedstore=9801; eCookieId=24389340-020b-467c-92bb-e643b49f5dd8; akacd_default=2147483647~rv=19~id=aa5de51f66c30911e891121bde1e27cb; RES_TRACKINGID=848601592390231; BVBRANDID=7d4ea9c3-d8fa-434e-b4e6-fada95400f3b; _pxhd=5680b06f38bc28a1e209f64fb96990d07e2275c45904881b3ac939f3d3d01b59:ee2bb167-1cf3-11ef-a294-f6798ac0b123; AZ_APP_BANNER_SHOWN=true; preferredStoreId=9801; TLTSID=83f834efafbc16549d0100e0ed6ab7dd; TLTUID=83f834efafbc16549d0100e0ed6ab7dd; az_bt_al=ade84ecf7ae84c01f285a3650ec27a16; rewardsId=; userVehicleCount=0; cartProductPartIds=; cartProductSkus=; cartProductTitles=; cartProductVendors=; cartUnitPrice=; cartCorePrice=; cartDiscountPriceList=; _pxdc=100; filterOpenStates=; _abck=47571064539E06B51520B3C2FAB7138D~0~YAAQrKlgaEVT9NWPAQAAvOHf1wt2DjrElo60Jled9kDwtJQJPVMdI8a+Trplv20fYn+i+0OaDLKWd0EPU5ih0IIggpdIVjL+GVpVn7iGkuvBGAWcKQYCn6wLDMiMRBkKNCYVJSWwxccn4gtAUfLjiNM06cuS0Lx9i24s4uKMD/BGqsxrjCxd8O0JLp7195V1ZO+/K2BmkZQsqOEQl3dAPeBO6VVlmzAWOMGOj/IKLiYFqs14KFq4N4NHPqGyaWOihpp7780sOfS5dwRToVDaCHgzz7JiZlA5JY3G9iKypHmvcAWifrakzYFTaPxE6e9cCxPs1Rv3GQKJcH186ympOfzagqKKzkdYJYpd64qRk0FUVbEWdFYH+o9+EyFCk4EXS+2hy/UWhNFvgbI0dYMkoZB0QZtONdVibCI=~-1~-1~-1; allSearchTerms=1124077%20%7C%201124101%20%7C%2025003; prevUrlRouteValue=%2Fsearchresult%3FsearchText%3D25003; redirect_url=%2Fsearchresult%3FsearchText%3D25003; JSESSIONID=mcnYRcBn2EFLiAsWSXzwaM1BPrTYY-22VctlCUVkEfUc5zhLVS5I!-1932607119; profileId=274732730280; OptanonAlertBoxClosed=2024-06-02T09:26:43.827Z; az_bt_cl=hPp0YAbH2l1Jzlm4TTBcIcYflum1zUX4unKJGwzKoHvjokFXHdYnlAWPIJvDgYZV; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Jun+02+2024+17%3A26%3A44+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=71bccfce-b3ff-4e43-8487-22057b2d7f94&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=JP%3B; sbsd=sSvqo02v247C2PPAUDbCQ+apf7ObcoJKwYRd3mzHZYUYCcugHW94/h3Xfk2dhYR/6BdBwXfrx1Zj6fQsPugxbME9Xo2scyAuDPIh1eRIwL/0h5SQ4qn0kFZsznrLMdS3YbWObyC7iQVkSrXN+gdhFIiKvVS8BYIBtlHStn3UDity9Mnum3MeKPGqEjA6jkpC6; bm_sz=56CA8F4B21CCEBAFB21D4ADF17985B35~YAAQLvAgF8G2ML6PAQAA9cK22BeaAqNMhhhkvK9vsQgtVlExY+Lzys43tKNFz43Fdg1M/TW0agnD47fLSF4PAkcWRCuG4HVxl5b011smZE1bPk/7T+2bizwJdnK+YRRSKn9TYB1xMBkHWQe+9YuuX+hIC8Qf4ldHdLIcYhMN33LrVkigzLU7mvPO4Dnktn2x6JlHIxWMclqL5b3oS9pnvEoTREvc9TQE5Hyz7c8dYZ63bNSeybyFpr5h0b+F+f1387arHXUFEJ9X7coUmAv1v+E6wXYPLFelOcnqsTjZ62HoyJ4UobCLRHoj+C0Wr6i84d9PtKJuGWzPXuqM94zUgtE1SVdyes00CAFNK+p37OItek8Tc/KP2GkNbi1Qtsb78JDm6uwkIyPzmFCc9q8btJtAdoM572SZzj1w6xxMpM5Np+Z5Kz1qkjK0UkhAryx7l1H+3sEr~4408368~3490867; ak_bmsc=F3D39F3B0EECB703CEF1F6E9A31B07D9~000000000000000000000000000000~YAAQLvAgFwG3ML6PAQAAbcS22Bd0LxBIc9FGfx7zdFztagXV3KxR8+ELvx/6GfrDyys9Cs1PoQKOS5QmA9P/TauiseaOEp6dqRpKen87FLnvDmK6kPaEUSyB1nNbMlVVQ4UdBZjjwpuYBy5Cg+CkIy75wDSlkOGYdpkHSeKCzV1kt5Vfs7R4uWaqCuBJGNU18GjJnTxCzi4TQ5oonQI8bK49W03jI3ASKebZPu8OnaKAhASWmhB5kM3MTXO+u6kW8lQ+zxt42blQAl9bgb9SqaW1dENeuP5/CNINjmJ2Q7GKQVJ+CaScHxXdgAItfj7ALhocT+buJLT9NET43NRLHFq1mubyGf2SEISQf/tvifYX6AaMAJgaYX+vAlyUlfIKduXG5ads+AVgzWipPA=='
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
    time.sleep(random.uniform(1,3))
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


