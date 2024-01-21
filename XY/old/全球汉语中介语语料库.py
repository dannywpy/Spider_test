import json

import requests
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(['语料背景信息', '所属课程','产出地点','产出日期','字数要求','文体','国籍','性别','年龄','现有文化程度','其他外语及程度','学习目的','作者类型','母语或第一语言','是否华裔','汉语水平等级','HSK等级','文本'])
header = {
    "Cookie":"PHPSESSID=11uee0g4kfnba8mke47cvrqit1; PHPSESSID_NS_Sig=oenCV6mfmD9l5BG7",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

data = {

    # "isDeptCheck": false,
    "ft": "",
    "tablename": "ylk_zi",
    "keystr": "比 还",
    "token": "e93e83997105251a82476c92929e77f4",
    "corp_org_id": "",
    "currpage": '',
    "pagesize": 50,
    "text": ""

}
for i in range(1,14):
    updated_data = data.copy()  # 创建 data 的副本
    updated_data["currpage"] = str(i)
    response = requests.post(url='http://qqk.blcu.edu.cn/corp/index/getzfcsample',headers=header,data=updated_data)
    reponse_data = response.text
    json_datas = json.loads(reponse_data)
    all_data = json_datas['data']
    for data_item in all_data:
        background = data_item['corpus_name']
        project = data_item['project']
        option_type = data_item['option_type']
        write_time = data_item['writetime']
        lower_limit = data_item['lower_limit']
        file_style = data_item['file_style']
        authornationality = data_item['authornationality']
        gender = data_item['gender']
        age = data_item['age']
        learn_option = data_item['learn_option']
        else_lan = data_item['else_lan']
        learningpurpose = data_item['learningpurpose']
        user_type = data_item['user_type']
        mothertongue = data_item['mothertongue']
        chinese_is = data_item['chinese_is']
        ext1 = data_item['ext1']
        shkgrade = data_item['shkgrade']
        text = data_item['content']
        sheet.append([background,project,option_type,write_time,lower_limit,file_style,authornationality,
                      gender,age,learn_option,else_lan,learningpurpose,user_type,mothertongue,chinese_is,ext1,shkgrade,text])


    workbook.save('比-还.xlsx')
    print(f'{i}successful')

















