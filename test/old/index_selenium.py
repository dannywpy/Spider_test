import time

from selenium import webdriver

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
import openpyxl

def open_file():
# 打开Excel文件
    workbook = openpyxl.load_workbook('old/test_2017.xlsx')

    # 选择一个工作表
    worksheet = workbook['Sheet1']

    # 读取第一列的数据
    column_data = []
    for column in worksheet.iter_cols(min_col=1, max_col=1, values_only=True):
        column_data = list(column)
    return column_data

def open_brows():
    url = 'https://deindex.h3c.com/2023/Insight/Cityinfo/'
    data=open_file()
    driver = webdriver.Chrome()

    driver.get(url)
    driver.maximize_window()
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, 'select2-selection__arrow').click()
    driver.find_element(By.CLASS_NAME,'select2-search__field').send_keys('2017')
    driver.find_element(By.CLASS_NAME,'select2-search__field').send_keys(Keys.ENTER)
    time.sleep(2)
    for cityname in data:
        if(cityname=="city"):
            continue;
        driver.find_elements(By.CLASS_NAME,'select2-selection__arrow')[1].click()
        driver.find_element(By.CLASS_NAME,'select2-search__field').send_keys(cityname)
        driver.find_element(By.CLASS_NAME,'select2-search__field').send_keys(Keys.ENTER)
        time.sleep(2)
        js_code = driver.execute_script("return document.documentElement.outerHTML")
        print(js_code)
        # driver.execute_script('window.scrollBy(0, 700)')
        # driver.find_elements(By.CLASS_NAME,'ranking-nav-icon')[0].click()
        # time.sleep(1)
        # driver.find_elements(By.CLASS_NAME, 'ranking-nav-icon')[1].click()
        # time.sleep(1)
        # driver.find_elements(By.CLASS_NAME, 'ranking-nav-icon')[2].click()
        # time.sleep(1)
        # driver.find_elements(By.CLASS_NAME, 'ranking-nav-icon')[3].click()
        #
        # time.sleep(1)

        # driver.find_elements(By.CLASS_NAME, 'ranking-nav-icon')[0].click()
        #


        time.sleep(2)
    #
    #
    #
    # time.sleep(4)

open_file()
open_brows()
























