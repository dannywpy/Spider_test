import time

from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.common import Actions
path =  r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # 请改为你电脑内Chrome可执行文件路径
co = ChromiumOptions().set_browser_path(path)
page = ChromiumPage(co)
page.get('https://www.waiglobal.com/us_en/amfinder')
ac = Actions(page)
page.ele('.chosen-single').click()
time.sleep(0.5)
page.ele('#finder_5__11_chosen').input('Hon')
time.sleep(0.5)
page.ele('#finder_5__11_chosen').input('d')












