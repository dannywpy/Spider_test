import requests

proxies = {
    "https": "http://183.152.223.34:3828"
}
req = requests.get('http://icanhazip.com/', proxies=proxies)
print(req.status_code)

# 访问 http://icanhazip.com/（https://icanhazip.com/） 可以得到你访问时的ip地址