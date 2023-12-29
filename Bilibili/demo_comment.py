import requests
import csv

f = open('../../Study_spider/BiliBili/date.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
        '姓名',
        '性别',
        '评论',
        'sign',
]
               )

csv_writer.writeheader()




headers = {
    "Cookie":"buvid3=F180D9CD-4B03-7702-2AC1-ED487039A5E175668infoc; b_nut=1699673175; i-wanna-go-back=-1; b_ut=7; _uuid=BC1A2173-9B10E-3398-101073-929996F2C710E89682infoc; enable_web_push=DISABLE; buvid4=5B3C8F2A-D43A-64AE-D06D-6618067767EC76724-023111111-OLMPg5n6UGp4%2BzkqYDfpjg%3D%3D; home_feed_column=5; browser_resolution=2048-1027; DedeUserID=305756799; DedeUserID__ckMd5=629699e6dc6c2231; rpdid=|(umu)~||klR0J'uYmmY~JkuJ; header_theme_version=CLOSE; fingerprint=e0871aa6d3240edceb62361bdb7ea709; buvid_fp_plain=undefined; CURRENT_QUALITY=116; LIVE_BUVID=AUTO4316998855272943; hit-dyn-v2=1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; bp_video_offset_305756799=872707311269838944; buvid_fp=e0871aa6d3240edceb62361bdb7ea709; PVID=5; b_lsid=71DC9BD6_18C5E61B1F5; SESSDATA=4a601c4d%2C1717942511%2Cacf58%2Ac2CjCRl5MHEhb5yjOBf_V-VYDukMELQEK80yUXSJVah07hCR-1Mmsw9B0Bv3O1-4zJjvoSVmotcW9JMVJ2d2x6OEV3clZSbnFXemdTaG1uYjVWdU9iRFVFYWl6MmRhb2VXcGROODVIdDFjQjBfOVJFLVVGNGIxbEtWVUZJRGc3WFphd21Obm5IT0NnIIEC; bili_jct=7b9b941ab9515f3750c2ab387b545be1; sid=5nshgq6i; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI2NDk3MzQsImlhdCI6MTcwMjM5MDQ3NCwicGx0IjotMX0.nktxc6ReV8n3kp3BwvU6_V-X654UFG5NNlxdErXWlhA; bili_ticket_expires=1702649674",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

}
url = 'https://api.bilibili.com/x/v2/reply/wbi/main?oid=796965778&type=1&mode=2&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=97cc0f405f8c7615d0a3ac8e816a2bd4&wts=1702390603'

respone = requests.get(url= url,headers= headers)

respon_json = respone.json()
print(respon_json)
breakpoint()
replies = respon_json['data']['replies']
for index in replies:
    username = index['member']['uname']
    message = index['content']['message'].replace('\n', ',')
    sex = index['member']['sex']
    sign = index['member']['sign'].replace('\n', ',')

    dit = {
        '姓名': username,
        '性别': sex,
        '评论': message,
        'sign': sign,


    }
    #csv_writer.writerow(dit)
    #print(dit)

    print(dit)






