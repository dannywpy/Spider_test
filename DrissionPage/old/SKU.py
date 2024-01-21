import csv
import time

from DrissionPage import ChromiumPage
f = open('starts.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['Part_Number','num'])
csv_writer.writeheader()
page = ChromiumPage()
page.get('https://www.autozone.com/batteries-starting-and-charging/starter?intcmp=CAT%3AFTR%3A1%3A20240501%3A00000000%3AGEN%3AAPTP-DLStarters&pageNumber=3')
for i in range(1,104):
    page.wait.load_start()
    page.scroll.to_location(0,4000)
    time.sleep(0.5)
    page.scroll.to_location(0, 6500)
    time.sleep(0.5)
    page.scroll.to_location(0, 3500)
    page.wait.load_start()

    skus = page.eles('.az_md')
    unique_links = set()

    for sku in skus:
        link = sku.link
        if link not in unique_links:
            unique_links.add(link)

            dit = {
                'Part_Number': link,
                'num':i
            }
            csv_writer.writerow(dit)


    print(f'successfully   =============={i}页')
    page.ele('@id=nextBtnLabel').click()
    time.sleep(2)
page.close()
