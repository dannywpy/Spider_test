import time

from DrissionPage import ChromiumPage
page = ChromiumPage()
page.get('https://kns.cnki.net/kcms2/article/abstract?v=MTbc36RhFpQ0JQF_3S-vY5hBYRS4hCe908cXk5C7yJZk5Rw475Jv8brCZEOh1cvPWupA2Ymz9SzDGVdNToFn8E6XjhpCBb_u18IjO59ghjL93GuueyaGaeutoGwtOtCl&uniplatform=NZKPT&language=gb')

time.sleep(3)
page.wait.load_start()
page.ele('#pdfDown').click()
time.sleep()



