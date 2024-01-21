
from selenium import webdriver
import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
# chrome://version/
options.add_argument(r"user-data-dir=C:\Users\D_Wang\AppData\Local\Google\Chrome\User Data")

f = open('data.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '价格', '评论', '店名', '详情页'])

csv_writer.writeheader()


driver = webdriver.Chrome(options=options)

driver.get('https://www.jd.com/')

driver.find_element(By.ID, 'key').send_keys('休闲鞋')

driver.find_element(By.CLASS_NAME, 'button').click()

driver.implicitly_wait(10)

def drop_down():

    for x in range(1, 12, 2):
        time.sleep(1)
        j = x / 9

        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j

        driver.execute_script(js)


def shop_info():

    drop_down()

    lis = driver.find_elements(By.CSS_SELECTOR, '.gl-item')

    for li in lis:
        """
        li --> <selenium.webdriver.chrome.webdriver.WebDriver...>
            提取具体每一个商品信息数据内容
        replace('\n', '') 字符串替换 把\n替换成空
        """
        try:
            # 标题
            title = li.find_element(By.CSS_SELECTOR, '.p-name-type-2 em').text.replace('\n', '')
            # 价格
            price = li.find_element(By.CSS_SELECTOR, '.p-price strong i').text
            # 评论
            commit = li.find_element(By.CSS_SELECTOR, '.p-commit strong a').text
            # 店名
            shop = li.find_element(By.CSS_SELECTOR, '.p-shop span a').text
            # 详情页
            link = li.find_element(By.CSS_SELECTOR, '.p-name a').get_attribute('href')
            dit = {
                '标题': title,
                '价格': price,
                '评论': commit,
                '店名': shop,
                '详情页': link,
            }
            # 写入数据
            csv_writer.writerow(dit)
            print(dit)
        except:
            pass


for page in range(1, 11):
    shop_info()

    driver.find_element(By.CLASS_NAME, 'pn-next').click()