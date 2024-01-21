import json
import time
import requests
import schedule
from time import sleep
from DZ import comment
def ip_get():
    while True:
        try:
            url = 'http://api.yilian.top/v2/proxy/proxies?token=JBkTKvn9gthLCBoB946aqo8wQSwzc6g61O&pull_num=1&format=json&protocol=1&separator=1&auto_shield=true'
            res = requests.get(url=url).text
            # 解析JSON数据
            data = json.loads(res)
            # 提取IP地址
            ip_addresses = data['data'][0]['ip']
            ip_port = data['data'][0]['proxy_port']
            # 打印提取的IP地址
            ip_all = f'{ip_addresses}:{ip_port}'
            proxies = {
                'http': 'http://' + ip_all,
                'https': 'http://' + ip_all
            }
            print(proxies)
            return proxies

        except Exception as e:
            print(str(e))
        finally:
            sleep(0.2)
def time_sleep():
    ip_get()
    schedule.every(115).seconds.do(ip_get)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == '__main__':
    time_sleep()