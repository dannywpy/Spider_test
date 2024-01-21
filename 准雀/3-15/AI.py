import pandas as pd
import requests
from lxml import etree
from openpyxl import Workbook
from wordcloud import WordCloud
import matplotlib.pyplot as plt
base_url = 'http://search.cnki.com.cn/Search/ListResult'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def get_page_text(url, headers, search_word, page_num):
    data = {
        'searchType': 'MulityTermsSearch',
        'ArticleType': '',
        'ReSearch': '',
        'ParamIsNullOrEmpty': 'false',
        'Islegal': 'false',
        'Content': search_word,
        'Theme': '',
        'Title': '',
        'KeyWd': '',
        'Author': '',
        'SearchFund': '',
        'Originate': '',
        'Summary': '',
        'PublishTimeBegin': '',
        'PublishTimeEnd': '',
        'MapNumber': '',
        'Name': '',
        'Issn': '',
        'Cn': '',
        'Unit': '',
        'Public': '',
        'Boss': '',
        'FirstBoss': '',
        'Catalog': '',
        'Reference': '',
        'Speciality': '',
        'Type': '',
        'Subject': '',
        'SpecialityCode': '',
        'UnitCode': '',
        'Year': '',
        'AcefuthorFilter': '',
        'BossCode': '',
        'Fund': '',
        'Level': '',
        'Elite': '',
        'Organization': '',
        'Order': '1',
        'Page': str(page_num),
        'PageIndex': '',
        'ExcludeField': '',
        'ZtCode': '',
        'Smarts': '',
    }

    response = requests.post(url=url, headers=headers, data=data)
    page_text = response.text
    return page_text


def list_to_str(my_list):
    my_str = "".join(my_list)
    return my_str


def get_abstract(url):
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    tree = etree.HTML(page_text)
    abstract = tree.xpath('//div[@class="xx_font"]//text()')
    return abstract


def parse_page_text(page_text):
    tree = etree.HTML(page_text)
    item_list = tree.xpath('//div[@class="list-item"]')
    page_info = []
    for item in item_list:
        # 标题
        title = list_to_str(item.xpath(
            './p[@class="tit clearfix"]/a[@class="left"]/@title'))
        # 链接
        link = 'https:' + \
               list_to_str(item.xpath(
                   './p[@class="tit clearfix"]/a[@class="left"]/@href'))
        # 作者
        author = list_to_str(item.xpath(
            './p[@class="source"]/span[1]/@title'))
        # 出版日期
        date = list_to_str(item.xpath(
            './p[@class="source"]/span[last()-1]/text() | ./p[@class="source"]/a[2]/span[1]/text() '))
        # 关键词
        keywords = list_to_str(item.xpath(
            './div[@class="info"]/p[@class="info_left left"]/a[1]/@data-key'))
        # 摘要
        abstract = list_to_str(get_abstract(url=link))
        # 文献来源
        paper_source = list_to_str(item.xpath(
            './p[@class="source"]/span[last()-2]/text() | ./p[@class="source"]/a[1]/span[1]/text() '))
        # 文献类型
        paper_type = list_to_str(item.xpath(
            './p[@class="source"]/span[last()]/text()'))
        # 下载量
        download = list_to_str(item.xpath(
            './div[@class="info"]/p[@class="info_right right"]/span[@class="time1"]/text()'))
        # 被引量
        refer = list_to_str(item.xpath(
            './div[@class="info"]/p[@class="info_right right"]/span[@class="time2"]/text()'))

        item_info = [i.strip() for i in
                     [title, author, paper_source, paper_type, date, abstract, keywords, download, refer, link]]
        page_info.append(item_info)
    # print(page_info)
    return page_info



def write_to_excel(info, search_word, wb, ws):
    title = ['title', 'author', 'paper_source', 'paper_type', 'date', 'abstract', 'keywords', 'download', 'refer', 'link']  # 设置表头

    if ws is None:
        ws = wb.active
        ws.title = search_word
        ws.append(title)

    for row in info:
        ws.append(row)

    return wb, ws

# 创建 Excel 文件对象
wb = Workbook()
ws = None

for i in range(1, 7):
    # 获取页面数据
    page_text = get_page_text(base_url, headers, '生成式人工智能', i)

    # 解析页面数据
    page_info = parse_page_text(page_text)

    # 将数据追加到 Excel 文件中
    wb, ws = write_to_excel(page_info, '生成式人工智能', wb, ws)
    print(f'第{i}页successfully')
# 保存 Excel 文件
wb.save('data.xlsx')
df = pd.read_excel('data.xlsx')
# 提取 'keywords' 列的数据
keywords = df['keywords'].dropna().astype(str)

# 将关键字合并成一个字符串
text = ' '.join(keywords)

print(text)
# 生成词云对象，设置中文字体
wordcloud = WordCloud(font_path = 'C:\\Windows\\Fonts\\simfang.ttf', width=800, height=400, background_color='white').generate(text)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# 保存词云图到指定路径
wordcloud.to_file(r'C:\Users\D_Wang\PycharmProjects\Spider_dome\准雀\3-15\生成式人工智能wordcloud.png')  # 指定保存的文件路径
plt.show()

