import select
import csv
import requests
import parsel
f = open('京东.csv',mode='a',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['价格',
        '名称',
        '店铺',])
csv_writer.writeheader()
header={
    "Cookie":"unpl=JF8EALBnNSttCh8EVk4CGBYRTl5SW1gJSB9XP2JWUlldGAdSGAMbERB7XlVdXxRLFB9sZhRUXlNOUg4ZBysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAh0UEk5fXFZdDXsWM2hXNWRUXENQARwyGiIRex8AAlkNSBYHbyoFUltaTlYNEwIeIhF7Xg; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ceabd125042744029ea4b754bbf20121|1703047699274; __jdu=1773439914; areaId=2; ipLoc-djd=2-2830-0-0; PCSYCityID=CN_310000_310100_0; pinId=-SR6s0XHaj78poOIm1QhqA; pin=jd_dzauqoDZpbke; unick=jd_dzauqoDZpbke; ceshi3.com=000; _tp=LUjlz5Xwfi6%2F8enPTmGlRA%3D%3D; _pst=jd_dzauqoDZpbke; jsavif=1; jsavif=1; shshshfpa=9f4f3596-c209-d0d1-fe3f-8002f8ed345a-1703047739; shshshfpx=9f4f3596-c209-d0d1-fe3f-8002f8ed345a-1703047739; rkv=1.0; qrsc=3; mba_muid=1773439914; wlfstk_smdl=y3qqv2plpszdx4wsluqnplmihtf280n7; TrackID=14vhcAEuvyHFtij-X9NDpUj1Y2nq6hTm4o_KjsHoKmwZr4HVeF_aaI2YCc9Xq33E1BVvrTCMTekpIHMScPzft5vTj7-hSoJ8I9VmhP46KsZ8; thor=F9A20C59B45033876AEF1563EC33F7C27402236A5B8A6C38B131572022111FDEB7D6B1B7A9124C2EF64633B214D9931778D0AACFE4E4598D44EF34454E3889BE8F6E46F8D4EB8342BBB14B956178FB1DDF08266E394266E951A18C0607A6AE290E53FAC1B2C1480FA726C1FE2B741E7F6AAA0841DB306624720973B337FED295CDC447F83CB78955841598A3848E8B4D157F6098A2E04E317205A3F44B227196; flash=2__749CPZ7utewQI8vITJ_ogNzYh7osDJo9cuDJjj-_1kyNScUJfoKmnDP7qqZXb6O0ApdW-qeMsUF_8SX-SeCNLbQW-8E-j3iyrr8fAMscgs*; avif=1; __jda=143920055.1773439914.1703047690.1703047699.1703050075.2; __jdc=143920055; 3AB9D23F7A4B3CSS=jdd03VOV4OKEHJIKVUVRIYBNGDSNK7I5H3S3DK3BPBSL7QX2IY77JLYKWQ33IRY453R7NV2E3FPPC7BKLMKW4YBJV65SQ64AAAAMMQXLOCMIAAAAADA24EXNGH3VBZUX; _gia_d=1; xapieid=jdd03VOV4OKEHJIKVUVRIYBNGDSNK7I5H3S3DK3BPBSL7QX2IY77JLYKWQ33IRY453R7NV2E3FPPC7BKLMKW4YBJV65SQ64AAAAMMQXLOCMIAAAAADA24EXNGH3VBZUX; __jdb=143920055.11.1773439914|2.1703050075; shshshsID=f89e9886a51880a4c9367ad01a2223fe_8_1703052542307; shshshfpb=AApjy1oWMEk81lsIJ0NH-P4AC-O00WhcDBHc5SgAAAAA; 3AB9D23F7A4B3C9B=VOV4OKEHJIKVUVRIYBNGDSNK7I5H3S3DK3BPBSL7QX2IY77JLYKWQ33IRY453R7NV2E3FPPC7BKLMKW4YBJV65SQ64",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


}

url= 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=shou%27ji&pvid=f4406a41f261455eab440955e715bea6'


responsse = requests.get(url=url, headers= header)

html_data = responsse.text

select_one = parsel.Selector(html_data)

goods = select_one.xpath('.//div[@class="gl-i-wrap"]')

for good in goods:
    price = good.xpath('string(.//div[@class="p-price"])').get("").strip()
    title = good.xpath('string(.//div[@class="p-name p-name-type-2"])').get("").strip()
    shop = good.xpath('string(.//div[@class="p-shop"])').get("").strip()

    with open('京东.csv',mode='a',encoding='utf-8',newline='') as f:
        csv.writer(f).writerow([price,title,shop])






















