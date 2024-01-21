#coding=utf-8
import requests
from IP import IP_GET
#请求地址
targetUrl = "https://myip.top"

#代理服务器
proxyHost = "110.42.9.74"        #代理IP
proxyPort = "50001"      #代理端口
proxyUser = "JBWRXMlaKg"  #代理账户
proxyPass = "JBp4S9VfFW"  #代理密码

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# Python3
proxyMeta = f"http://{proxyUser}:{proxyPass}@{proxyHost}:{proxyPort}"

proxies = {
    "http"  : proxyMeta,
    "https"  : proxyMeta
}

resp = requests.get(targetUrl, proxies=proxies)
print("Use proxies:", proxies)
print("Respose status code: ", resp.status_code)
print("Respose content: ", resp.text)