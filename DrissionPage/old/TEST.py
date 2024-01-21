import csv
import time
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.autozone.com/batteries-starting-and-charging/starter?intcmp=CAT%3AFTR%3A1%3A20240501%3A00000000%3AGEN%3AAPTP-DLStarters&pageNumber=1')

for i in range(0,3):
    page.scroll.to_location(0,4000)
    page.wait.load_start()

    # skus = page.eles('.az_md')
    # unique_links = set()
    # for sku in skus:
    #     link = sku.link
    #     if link not in unique_links:
    #         unique_links.add(link)
    #         print(link)

    page.ele('#nextBtnLabel').click()
    time.sleep(2)
page.close()
