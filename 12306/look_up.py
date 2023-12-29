import requests
import json
import prettytable as pt
url="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2023-12-27&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=GIW&purpose_codes=ADULT"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie":"_uab_collina=170331790099257306996242; JSESSIONID=8CE785CF037285227F77FEB5A6FA7D16; BIGipServerpassport=921174282.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1944584458.64545.0000; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2023-12-27; _jc_save_toDate=2023-12-23; _jc_save_wfdc_flag=dc; _jc_save_toStation=%u8D35%u9633%2CGIW"


}

response = requests.get(url, headers=headers)

# print(response.text)

response_json = response.json()

data = response_json['data']['result']
ta = pt.prettytable()
ta.field_names = [
    '序号',
    '发车时间',
    '到达时间',
    '用时',
    '硬卧',
    '一等座',
    '二等座'
                  ]
page = 1
for i in data:
    index = i.split('|')
    page = 0
    train_number = index[3]
    start_time = index[8]
    end_time = index[9]
    wait_time = index[10]
    hader_sleeper = index[28]
    first_class = index[31]
    second_class = index[30]
    dit={
        'train_number': train_number
        ,'start_time': start_time
        ,'end_time': end_time
        ,'wait_time': wait_time
        ,'hader_sleeper':hader_sleeper
        ,'first_class':first_class
        ,'second_class':second_class

    }
    ta.add_row([
    page,
    train_number
    ,start_time
    ,end_time
    ,wait_time
    ,hader_sleeper
    ,first_class
    ,second_class
    ])

    print(dit)









































































































































































































































