



# 导入模块
from selenium import webdriver
import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument(r"user-data-dir=C:\Users\D_Wang\AppData\Local\Google\Chrome\User Data")
# 创建文件对象
f = open('data.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '价格', '评论', '店名', '详情页'])
# 写入表头
csv_writer.writeheader()
"""
selenium --> 浏览器驱动 --> 浏览器
1. 打开浏览器
    - webdriver.Chrome() 谷歌浏览器
    - webdriver.Firefox() 火狐浏览器
    - webdriver.Edge() Edge浏览器

<selenium.webdriver.chrome.webdriver.WebDriver (session="992030c70cd41ced37040d8bdcea73a4")>
如果没有驱动或者驱动版本不对, 会报错的!
    驱动放到哪里:
        1. python安装目录里面  <代码可以不用写路径>
        2. 任意位置 <代码需要写路径>
        
3. 输入关键字, 进行搜索
    输入内容 --> 输入框里面进行操作
        先定位元素<根据元素面板标签>, 然后进行操作 <输入 点击 滑动 获取数据>
    - find_element_by_class_name() 按类名去查找元素
    - find_element_by_id() 按 ID 查找元素
    - find_element_by_css_selector() 通过css选择器查找元素

4. 进入商品列表页面 浏览数据 <商品信息获取下来>
    通过元素定位 --> 返回的是一个 []
        100%是没有获取到数据 --> 原因是什么?
            因为网页数据内容还没加载完成 --> 我就要获取数据?
隐式等待 driver.implicitly_wait(10) --> 10秒钟
    你什么时候加载完网页, 就运行下面的内容
死等 time.sleep(10)
    一定要等够10秒钟

"""
# 实例化浏览器对象 --> 打开浏览器
driver = webdriver.Chrome(options=options)
# 访问网址
driver.get('https://www.jd.com/')
# 定位搜索框 --> 进行操作
driver.find_element(By.ID,'key').send_keys('平板')
# 定位搜索按钮 --> 进行点击操作
driver.find_element(By.CLASS_NAME,'button').click()
# 进入到新的页面的时候, 可以做延时等待
driver.implicitly_wait(10)
# 下滑网页页面数据 --> 使用selenium执行JS代码
def drop_down():
    """执行页面滚动的操作"""  # javascript
    for x in range(1, 12, 2):  # 1 3 5 7 9  在你不断的下拉过程中, 页面高度也会变的
        time.sleep(1)
        j = x / 9  # 1/9  3/9  5/9  9/9
        # document.documentElement.scrollTop  指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        # selenium执行JS代码
        driver.execute_script(js)

def shop_info():
    # 调用函数
    drop_down()
    # 获取商品数据信息 --> 先获取所有商品信息对应标签 <列表>
    lis = driver.find_elements(By.CSS_SELECTOR,'.gl-item')
    # for循环遍历,把列表里面元素一个一个提取出来
    for li in lis:
        """
        li --> <selenium.webdriver.chrome.webdriver.WebDriver...>
            提取具体每一个商品信息数据内容
        replace('\n', '') 字符串替换 把\n替换成空
        """
        try:
            # 标题
            title = li.find_element(By.CSS_SELECTOR,'.p-name-type-2 em').text.replace('\n', '')
            # 价格
            price = li.find_element(By.CSS_SELECTOR,'.p-price strong i').text
            # 评论
            commit = li.find_element(By.CSS_SELECTOR,'.p-commit strong a').text
            # 店名
            shop = li.find_element(By.CSS_SELECTOR,'.p-shop span a').text
            # 详情页
            link = li.find_element(By.CSS_SELECTOR,'.p-name a').get_attribute('href')
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
    # 点击下一页
    driver.find_element(By.CLASS_NAME,'pn-next').click()