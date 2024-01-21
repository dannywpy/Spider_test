#coding=utf-8
from time import sleep

import requests
def ip_get():
    #请求地址
    targetUrl = "https://myip.top"

    #代理服务器
    proxyHost = "110.42.9.74"        #代理IP
    proxyPort = "50001"      #代理端口
    proxyUser = "JBWRXMlaKg"  #代理账户
    proxyPass = "JBp4S9VfFW"  #代理密码

    proxyMeta = f"http://{proxyUser}:{proxyPass}@{proxyHost}:{proxyPort}"

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }
    return proxies

print(ip_get())















