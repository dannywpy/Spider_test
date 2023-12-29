import time

import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

webdriver = webdriver.Chrome()
webdriver.maximize_window()
webdriver.get("https://deindex.h3c.com/2021/Insight/Cityinfo/")

time.sleep(3)

click = webdriver.find_elements(By.CLASS_NAME, 'select2-selection__arrow')[1].click()
time.sleep(1)

SELECT_city = webdriver.find_element(By.CLASS_NAME,'select2-search__field').send_keys('北京')
chose = webdriver.find_element(By.CLASS_NAME,'select2-search__field').send_keys(Keys.ENTER)
time.sleep(2)

def basic():

    text = webdriver.find_element(By.XPATH,'.//div[@id="cityInfoLv2"]').text
    print(text)

basic()





