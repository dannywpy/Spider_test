import csv
import json
import time

import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from matplotlib import pyplot as plt

ua = UserAgent()
f = open('沪深股市.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['股票代码', '股票名称', '当前价', '涨跌额', '涨跌幅', '年初至今', '成交量', '成交额', '换手率', '市盈率', '股息率', '市值'])
csv_writer.writeheader()
def get_data():
# 网页 URL
    for page_number in range(1,57):
        url = f"https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page={page_number}&size=90&order=desc&order_by=percent&market=CN&type=sh_sz"
        headers = {
        'User-Agent': ua.random,
            "Cookie":"xq_a_token=ea6ef3abf0b64fa4ec4343c5608361ed54114204; xqat=ea6ef3abf0b64fa4ec4343c5608361ed54114204; xq_r_token=38fbe8417b7b1b21f8f4c0a40a8e75e1f538990a; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxNzU0ODcxMCwiY3RtIjoxNzE1NzgzOTkyMzk3LCJjaWQiOiJkOWQwbjRBWnVwIn0.U8ICY3o5QVMVH6yVz-8liGEAj1N7ZD5_hFjHv7Y6rmSXiwdlNVdxZx-zxxyPDdUqtF-5wk2rVeCo0-B7jEif7kNOIRs3HSq5_XfpXZU056R75k-WndbSj_ku2vRL9DHn_7N1MG4-IVX-7OfCgfmVJP7mmNDR0KtgPfFph7T6mmQ1ImkSEq5mtvpPHhUmharihtyHHgDZ6ZtyDSC7rr3tL1NLn5iZ82eLe6-TN36OaDihF7scsotJPe9CvECtCimSQU9ToxDl2ZbzIQ5-BxGECFtf0JABhf5F56NRs0z1H-Ff1507t7YMv-Rmo0FL-MTqvcCnPVus91QeD-T78_SVsw; cookiesu=101715784018814; u=101715784018814; device_id=00135b5d7803fbc2d35b92214dedc062; Hm_lvt_1db88642e346389874251b5a1eded6e3=1715784020; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1715784020"
        }
        # 使用 requests 库获取网页 HTML 内容
        time.sleep(2)
        response = requests.get(url,headers=headers).text
        js_data = json.loads(response)
        items = js_data['item']
        for i in items:
            stock_code = js_data['data']['list'][i]['symbol']
            stock_name = js_data['data']['list'][i]['name']
            current = js_data['data']['list'][i]['current']
            chg = js_data['data']['list'][i]['chg']
            percent = js_data['data']['list'][i]['percent']
            cueent_year_percent = js_data['data']['list'][i]['current_year_percent']
            volume = js_data['data']['list'][i]['volume']
            amount = js_data['data']['list'][i]['amount']
            turnover_rate = js_data['data']['list'][i]['turnover_rate']
            pe_ttm = js_data['data']['list'][i]['pe_ttm']
            dividend_yield = js_data['data']['list'][i]['dividend_yield']
            market_capital = js_data['data']['list'][i]['market_capital']
            dit = {
                    '股票代码':stock_code,
                   '股票名称':stock_name,
                   '当前价':current,
                   '涨跌额':chg,
                   '涨跌幅':percent,
                   '年初至今':cueent_year_percent,
                '成交量':volume,
                '成交额':amount,
                '换手率':turnover_rate,
                '市盈率':pe_ttm
                , '股息率':dividend_yield,
                '市值':market_capital
                   }

            csv_writer.writerow(dit)
        print(f"{page_number} successfully")

def plt_pie():
    df = pd.read_excel('沪深股市.xlsx')

    # 提取股票名称和市值列
    stock_names = df['股票名称']
    market_values = df['市值']

    # 创建饼状图
    plt.figure(figsize=(10, 6))
    plt.pie(market_values, labels=stock_names, autopct='%1.1f%%', startangle=140)

    # 添加标题
    plt.title('各股票市值占比')

    # 显示图表
    plt.show()

def descr():
    df = pd.read_excel('沪深股市.xlsx')
    market_values = df['涨跌额']

    # 计算市值的最大值、最小值、均值和中位数
    max_market_value = market_values.max()
    min_market_value = market_values.min()
    mean_market_value = market_values.mean()
    median_market_value = market_values.median()

    # 打印结果
    print(f"涨跌额的最大值为: {max_market_value}")
    print(f"涨跌额的最小值为: {min_market_value}")
    print(f"涨跌额的均值为: {mean_market_value}")
    print(f"涨跌额的中位数为: {median_market_value}")

    # 定义数据并确保所有元素为浮点数
    values = np.array([max_market_value, min_market_value, mean_market_value, median_market_value], dtype=float)
    labels = ['最大值', '最小值', '均值', '中位数']

    # 创建柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=['blue', 'green', 'red', 'purple'])

    # 添加标题和标签
    plt.title('涨跌额统计数据可视化')
    plt.xlabel('统计类型')
    plt.ylabel('涨跌额')

    # 在每个柱形上显示具体数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom')

    # 显示图表
    plt.show()
def des1():
    # 从Excel文件中读取数据
    df = pd.read_excel('沪深股市.xlsx')
    market_values = df['涨跌额']

    # 计算涨跌额的最大值、最小值、均值和中位数
    max_market_value = market_values.max()
    min_market_value = market_values.min()
    mean_market_value = market_values.mean()
    median_market_value = market_values.median()

    # 打印结果
    print(f"涨跌额的最大值为: {max_market_value}")
    print(f"涨跌额的最小值为: {min_market_value}")
    print(f"涨跌额的均值为: {mean_market_value}")
    print(f"涨跌额的中位数为: {median_market_value}")

    # 定义数据并确保所有元素为浮点数
    values = np.array([max_market_value, min_market_value, mean_market_value, median_market_value], dtype=float)
    labels = ['最大值', '最小值', '均值', '中位数']

    # 创建折线图
    plt.figure(figsize=(10, 6))
    plt.plot(labels, values, marker='o', color='b', linestyle='-')

    # 添加标题和标签
    plt.title('涨跌额统计数据可视化')
    plt.xlabel('统计类型')
    plt.ylabel('涨跌额')

    # 在每个点上显示具体数值标签
    for i, value in enumerate(values):
        plt.text(i, value, f'{value:.2f}', ha='center', va='bottom')

    # 显示图表
    plt.show()

def new():
    # 读取Excel文件中的数据
    df = pd.read_excel('沪深股市.xlsx')

    # 提取当前价最低的6个和最高的6个股票
    lowest_prices = df.nsmallest(6, '当前价')
    highest_prices = df.nlargest(6, '当前价')

    # 提取最低价股票的名称和当前价
    lowest_stock_names = lowest_prices['股票名称']
    lowest_current_prices = lowest_prices['当前价']

    # 提取最高价股票的名称和当前价
    highest_stock_names = highest_prices['股票名称']
    highest_current_prices = highest_prices['当前价']

    # 创建最低价股票的条形图
    plt.figure(figsize=(12, 6))
    bars = plt.bar(lowest_stock_names, lowest_current_prices, color='blue')
    plt.title('当前价最低的6个股票')
    plt.xlabel('股票名称')
    plt.ylabel('当前价 (元)')
    plt.xticks(rotation=45)

    # 添加标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

    # 创建最高价股票的条形图
    plt.figure(figsize=(12, 6))
    bars = plt.bar(highest_stock_names, highest_current_prices, color='red')
    plt.title('当前价最高的6个股票')
    plt.xlabel('股票名称')
    plt.ylabel('当前价 (元)')
    plt.xticks(rotation=45)

    # 添加标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    new()















