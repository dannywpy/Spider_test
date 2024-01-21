import DrissionPage
from DrissionPage import WebPage

page = WebPage()
page.get('https://www.oreillyauto.com/detail/c/ultima/alternators---starters/starter/dad3c6651e74/ultima-starter-remanufactured/ost0/r612249a?pos=2')
page.wait.load_start()
page.ele('.product-list_title js-plp-list-dropdown js-compatibility').click()
page.wait.load_start()
vehicles = page.eles('.open-vehicle-table')

for vehicle in vehicles:
    vehicle.click()
    page.wait.load_start()
    di = page.ele('.compatibility-models')
    print(di.attrs)
    # full_vehicle = page.eles('.full-vehicle')
    # for full_ve in full_vehicle:
    #     page.wait.load_start()
    #     years = page.eles('.year-item')
    #     for year in years:
    #         ye = year.text
    #         print(full_ve.text,ye)













