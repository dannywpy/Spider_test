import csv
import time

import pandas as pd
from DrissionPage import ChromiumPage
from DrissionPage._configs.chromium_options import ChromiumOptions
from DrissionPage.errors import ElementNotFoundError

page = ChromiumPage()
# path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
# co = ChromiumOptions().set_browser_path(path)
# page = ChromiumPage(co)
df = pd.read_excel('link2.xlsx')
links = df['ln']
parts = df['part']
f = open(f'test1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f,fieldnames=['part','link','models','year','make'])
for link,part in zip(links,parts):
    time.sleep(5)
    page.get(link)
    # time.sleep(5)
    page.wait.load_start()
    time.sleep(1)
    page.scroll.to_location(0, 4000)
    time.sleep(0.5)
    page.scroll.to_location(0, 6500)
    time.sleep(0.5)
    try:
        page.ele('@class=product-list_title js-plp-list-dropdown js-compatibility').click()
        vehicles = page.eles('.open-vehicle-table')
        for vehicle in vehicles:
            page.listen.start('oreillyauto.com/product')
            print(vehicle.text)
            time.sleep(2)
            vehicle.click()
            data_packet = page.listen.wait()
            text = data_packet.response.body
            details = text["compatibleModels"]
            for models in details:
                years = details[models]
                for year in years:
                    dit = {
                        'part': part,
                        'link': link,
                        'year': year,
                        'models': models,
                        'make': vehicle.text

                    }
                    csv_writer.writerow(dit)
        print(f'succesfully ==================={link}')
    except ElementNotFoundError:
        print(f'Element not found++++++++++++++++++++++++{link}' )





