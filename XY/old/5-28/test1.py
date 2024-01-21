import csv
import json
import re
import requests
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
, 'Cookie':'AZ_APP_BANNER_SHOWN=true; mt.v=5.808966057.1716899646541; preferedstore=9801; preferredStoreId=9801; eCookieId=24389340-020b-467c-92bb-e643b49f5dd8; TLTSID=8058ae68afbc16549d0100e0ed6ab7dd; TLTUID=8058ae68afbc16549d0100e0ed6ab7dd; akacd_default=2147483647~rv=19~id=aa5de51f66c30911e891121bde1e27cb; az_bt_al=1b5ced86017ed7e0e59a02e62775c8fd; rewardsId=; RES_TRACKINGID=848601592390231; userVehicleCount=0; cartProductPartIds=; cartProductSkus=; cartProductTitles=; cartProductVendors=; cartUnitPrice=; cartCorePrice=; cartDiscountPriceList=; BVBRANDID=7d4ea9c3-d8fa-434e-b4e6-fada95400f3b; _abck=47571064539E06B51520B3C2FAB7138D~0~YAAQO/AgF1dcFamPAQAAkIcyvwvYNhiQah2iGf4Eewc8Z1UDI9hfD6ar/seCrf3kgxTp4FTqodNDwZxN+yqM1rj3tcIUSAKsR9gr79TmK4hxZ/9dufm+1Raah6/tT7M7Pem12sw0ut4L3iTpeyhme1CC4pztCh+95ee0G+s0RzkMJ7I7/D+EWuyLHBn0oT13Ox9rrCdeoOhCr1vYPALYtexBJANQ/t0PWBQZSgmdRXrif8kKmGuzR0DmwZgVFe0wS1DMAenBlyc9s+AdohfyqLIwpMtS5KprofIAE/IYXK3/2Is+WjIxY282INMA9n0x7KBInvB7yz9eKYYOHBjuba4irJJHuJwdjFtCEMOErwasaWGOaT3cUPwrcO7QQKOeAA/2L8GuoJ/5zQpkcI1JVYu7cuG9dNmdcDo=~-1~||0||~-1; userType=3; nddMarket=MEM%2C%20TN; nddHub=110; nddStore=6941; availableRewardBalance=0; _pxhd=5680b06f38bc28a1e209f64fb96990d07e2275c45904881b3ac939f3d3d01b59:ee2bb167-1cf3-11ef-a294-f6798ac0b123; sbsd_ss=ab8e18ef4e; prevUrlRouteValue=%2Fbatteries-starting-and-charging%2Fstarter%2Fp%2Fduralast-starter-19082%2F265620_0_0%3Frrec%3Dtrue; redirect_url=%2Fbatteries-starting-and-charging%2Fstarter%2Fp%2Fduralast-starter-19082%2F265620_0_0%3Frrec%3Dtrue; _pxdc=0; JSESSIONID=U8-_p_2ZtuZMh6IlPAu0a8Kzwg6HF4XwPIFg4y2ZeXPJBiZnh3Dr!-1850769494; WWW-WS-ROUTE=ffffffff09c20e6845525d5f4f58455e445a4a4216ce; bm_mi=B9A63559865372EF77F028052694A089~YAAQO/AgF5UML6mPAQAAowiovxfk6CLmQwLduJ0p9bCMVPQmUrofh4nW16ugoRfzwDVcMnunjLXVxUo6xbLbYD9y1AjNWZzzMLb1btxjXzb+HA5OawJHtrIUD6zYoaJssSyYcfOYMVyp8XUK6rbc785DIf8vW0ZRWVQGcP1RTJbHQcjG6QCtpfY7z/kftyVeNDtUyDY1z/cD+hd+JP/eNV7Gbe64N6PWmac2FvSFaZaLEmfrJkZD+HCmRbC2iRFrD69RHU++exyopc8EAKtqARj/Qg9xSV/q4gpip/uIX/tVq1pIj6F233YqaGoRXWdI5vQW2c3Xf9HgCUNgt7Mx77oxklXSpCbRoDQZgKbcPZ4PlaiAn0K1pTAs6QKDhxCkqeiBhPN9rUNCTYP4wXVgHWEXjv9F0j8AUgcm~1; bm_sz=A0BD35C1A16DB8BE5CBDBD18E21DFC94~YAAQO/AgF5cML6mPAQAAowiovxf3NdIn5A3Vjw+/X/0m0oU/xN998i4NVoT4lWhoLkcJ9xaBFyEluoTSsmYP7O/s99yj++mzhqxQJRJ7mIyZ9JKaix8YHC80m6J+0yhdxdwDCbVtW8x61QRuSSqqhTd0OVsiplCExwmQn2Td1c6CsDvZbbysWs9Mlc2dYdmj4ye0UWLFO0DK+FSuudJuEz913rCrt3wNb+qeblcXkRfcsz58q2DtUYAONeTHfdOiXOoIHrJH4q0gGLWdPEs5YazhLoPsbGryODKL+ibuiu5h+cN6zxoVvdFNLzZ7Edg8KRgf71Vw5bRLRC8ZPMVoC4ucKh5RpZ5WLs4Y0FRfIz3L8i8weFVF84UzPjOCv9wlpmznnbaWtXAMz5O4pv8zQNcy5qF8uXPyrIV7OaB5LdnsIUJqRWQ1oYYKvaqbpLDhI7Z8HUbFuN81Vayo+2Z0vQ==~4536629~3556933; az_bt_cl=hPp0YAbH2l1Jzlm4TTBcIX+pbHdnOlNaRCWuvbKWkdfGSO7ZQlD/GlHcjyNjGgxE; profileId=274394566520; ak_bmsc=5BBF4E6EBA2CE39BA0C74C8C43A9B0D9~000000000000000000000000000000~YAAQO/AgF1EOL6mPAQAAGROovxdkPTAR7lJdl/maEuvnGo26sLSdBNrSl+NirBk/Qasxvl3IgE7IwDa1pNvpgmZ3I8T2AwAPUNodWl+wzTwc+ogL5Iv5KNhB46lX+YHlwPVKqPu68eVWnZ6god1jHow1s3/XQZ5x9YF9cX8LJRhs9BjV8fULEZjGvx8KAX6YeoiY3+c54FiHwY04Ri9MjLqq067YfqjZpJSqtGlY02wyvCdrVkZ1HfY6/K0eVAVP3dl9ucfG2RxAaPzJuhaOL2Vuynwss+9CM8+f60fbytVnJZVI8vQWRisc9SULJHiWszex3ubvJKc6rCSq6Y3GQgHwdPTqUrAPjELHlQJsXeU2fmKLo6K3NcmwwfKD4PN5U5Aq5ruxymmqe46pqf1dAoQw/61O28ZevmNo9rFyKFpaVUV0D3CPNjv+G4p4vnXl/kaa+aOpk0C5iKe4W8elMT8mBGN2FyQrHnGPlMmNWaDWaZJKiEUkw03k0JWVsGa79SBwLXONs/VwKt3gU+A4MAwHXSxUjtk18pYnQ8TDGj8j5vp6hR49U+pTFldUqMy0Id7wT+sj7cFAwJyS9g==; bm_sv=3EDF41107269679856725247620CFAF6~YAAQO/AgF9gOL6mPAQAAhhWovxdbaFxeDEfZZ8xL8QRkKKD2OOWNZq3XOdL9Bu5trtHue7do9H0d8gN6Zgw+fMpeB59qqOUzkOLsAVgWzCnPXJpvujSStt+vhvw0rZQphRMrPHMYeUK1ICCAdo/hg/xT4B+aZW5fBLZh8Sfz/9HqZJ4FlHSY8/Y4oo2pM8QzaNl7+MdBunL+noe3e+RXw+1MRkI33n5h2GCMJ7J1xYolP7JQM5A6CtNeD/E+bIrcxjI=~1; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+28+2024+22%3A43%3A35+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=71bccfce-b3ff-4e43-8487-22057b2d7f94&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false; BVBRANDSID=5e072b07-0373-4e2a-a862-1fd68a6a23f2; sbsd=sH172ABZUBIQnw6bVWG4J/AN21T/yja5sefZnX0DdQ4hu+gzLDvU6aQuLH3+ZBKjs+NxnA9ydaTItXKerPlBoxihr4Aj9cp39f8sJNqXoGjogA085hrWdEj/hL9vxcSXxaZviiPVzht6lfxrn8YB3zQpi+VD6LchUetcu6LGCbC8fC6/UjPTVWcuqYoAxJQ55'

}

def extract_numbers_from_url(url):
    pattern = r'\d+'
    numbers = re.findall(pattern, url)
    return numbers

def get_vehicle_data(part_number, product_id):
    base_url = f"https://www.autozone.com/external/product-discovery/product/v1/products/{product_id}/fitments"

    params = {
        "country": "USA",
        "customerType": "B2C",
        "salesChannel": "ECOMM",
        "preview": "false",
        "lineCode": 'WWD',
        "partNumber": part_number
    }

    query_string = urllib.parse.urlencode(params)
    full_url = f"{base_url}?{query_string}"
    response = requests.get(url=full_url, headers=headers)
    js_data = response.json()

    vehicle_data = []
    for vehicle in js_data:
        make = vehicle['name']
        params['vehicleMake'] = make

        query_string = urllib.parse.urlencode(params)
        full_url = f"{base_url}?{query_string}"
        response = requests.get(url=full_url, headers=headers)
        js_data = response.json()

        for model in js_data:
            model_name = model['name']
            params['vehicleModel'] = model_name

            query_string = urllib.parse.urlencode(params)
            full_url = f"{base_url}?{query_string}"
            response = requests.get(url=full_url, headers=headers)
            js_data = response.json()

            for year in js_data:
                year_name = year['name']
                params['vehicleYear'] = year_name

                query_string = urllib.parse.urlencode(params)
                full_url = f"{base_url}?{query_string}"
                response = requests.get(url=full_url, headers=headers)
                js_data = response.json()

                details = [detail['name'] for detail in js_data]
                vehicle_data.append({
                    'Part_Number': part_number,
                    'Make': make,
                    'Model': model_name,
                    'Year': year_name,
                    'details': ', '.join(details)
                })

    return vehicle_data

def main():
    url = input("请输入URL: ")
    numbers = extract_numbers_from_url(url)

    if len(numbers) >= 2:
        part_number = numbers[0]
        product_id = numbers[1]

        if part_number.isdigit():
            vehicle_data = get_vehicle_data(part_number, product_id)

            with open('test12.csv', mode='w', encoding='utf-8', newline='') as f:
                fieldnames = ['Part_Number', 'Make', 'Model', 'Year', 'details']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(vehicle_data)
        else:
            print("Part number is not a digit.")
    else:
        print("URL does not contain enough numbers to create a Product object.")

if __name__ == "__main__":
    main()
