import re

import requests
from bs4 import BeautifulSoup

url = 'https://www.sou-yun.cn/QueryPoem.aspx'

data = {
'__VIEWSTATE': '/wEPDwUKLTI0NDYyODg3MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFDklzUHJlY2lzZU1hdGNoBRVTaG93TWF0Y2hlZENsYXVzZU9ubHkniVJ0CzhUakhDPh3PFb0IQ8cTufqwPKGrAoa+LWtizQ==',
'__VIEWSTATEGENERATOR': '0C7ECFE8',
    '_TitleKeys': '',
'_ContentKeys': '街西 池馆',
'KeywordTextBox': '温庭筠',
'QueryButton': '检索',
'SearchScope': 'poem',
'StartInClause': '0',
'AuthorKeyword': '',
'DynastyOption': '0',
'PTypeOption': 'ALL',
'RhymeCategory':''
}


headers = {
    'Cookie':'did=5e6bed80-ce5e-4856-bc77-750bcefbe721; SECKEY_ABVK=56iqOhlIuTjJJ2Mte1yw5yuLYYi5y5VDnvYUU08vUg3X/Bc6Cpj9T49njhxuWuovUEgaGr91wmchrI1VUlEbOA%3D%3D; jdt=eyJraWQiOiI3NDdlYWE1ZDAxMmEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJLOHgwbm41MFZ5OSIsImF1ZCI6IjE1NTY0OGNkYTZkMDliM2YiLCJuYmYiOjE3MTY4MTQzODYsImV4cCI6MTcxOTQwNjM4NiwidXNlcl9pZCI6ImVmNmIyYzM1LWZiOGEtNGNlZC1hZjQxLTZhYWQwOGM1MDBjNCIsImlhdCI6MTcxNjgxNDM4Nn0.AtiGMEvcKL9EMCQdgb_2zkVBWL10w40rTB3oaAlALvEOkIfOM95PwpqpGlxE86NRx2k5rPlsh9TzZbrllHDnsqRmb-yF4dwlDG_4LefhkEuUE9-UnzQOhuZqvU4KuMOthyYCDBn73p8WKiJ4k9CJ88HzHLDMNh6yoVN-47YdnCXZvIoXkWX4RBd0dzGHLPnGOpbpWvUETEuDLu1INvT3xtnLtAK0ngYvSlX4U4QITeTiCrIFD9qVVd3-cDsryC59pOTbNnJpxNEssizdoAtH1-YIjYAtHzsJR8qZ-0NbNYbWl5cbvqbl8Coe8t6vPQDVG311cDc2YXU2HkrvArBwvuZ21cG93AxRbGeha2wnZSIKNGXNB3HaX40b17uHN5_mpVCTWovSdWN0jPDAUn0TQK506Q_7GFjpHBJMJnFHZURytc1eqbywAqHFUPqwppQsM6AIbE66sKXwljyaxlXl-la9iZDsJk3CDwtrxLUvqvYWTYxwcROZHSEaFRiqmkU9HAmpWQO2TowY_xIog77T8Ecz1NQkpa0_a_RSil1uXUCr8bYMtbE7Pl1KsFaW7Q6Ul3d3od0KnyK5rKUFLkGG3xtcsRzcMxFpvs_YKcQZITR1nWyiQUn3W0cSeSbIRFrSUD7ZLHMhDGIrSSiVenXJ1j_neH3UAn1dxLdUCrc_vCA; BMAP_SECKEY=56iqOhlIuTjJJ2Mte1yw5yuLYYi5y5VDnvYUU08vUg09bLDpIq5K2clXzdgI5R8060ebxsvp_VYRUP5H27s0gPSBWRDoNWjeUSiJBBxRWreQoGmnxrO5ndodVG81q4TxxESCWLG7H7PlNDBKLZrskQoYZY7uHm1u7iCwCCeKj1EnbZEWymBpwU2G5bOFn7oeLpi0P3C1tCNe9FBXFTyyIQ; _gid=GA1.2.297304238.1716814386; lpt=1716814386753; displayedPAIDs=61e2f324856f5f0fd4b52b71.1716814391593; _ga_THLRK7E3FF=GS1.1.1716818185.2.1.1716818185.60.0.0; _ga=GA1.2.702538123.1716814386; _gat_gtag_UA_19814235_1=1; __gads=ID=5ec6b154f261a95d:T=1716814386:RT=1716818186:S=ALNI_MYutz-khmLoc8tsVrsdgcEoN1eS8g; __gpi=UID=00000e305408328d:T=1716814386:RT=1716818186:S=ALNI_MZe1og-FhHsG0WKiNfoIiyNM_778Q; __eoi=ID=10cb8a26b1cc1061:T=1716814386:RT=1716818186:S=AA-Afjba4_5ktFJcec0OUqTzthya',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.post(url=url,data=data,headers=headers).text

soup =  BeautifulSoup(response, 'html.parser')

titles  = soup.find_all('a',class_='poemCommentLink')
authors = soup.find_all('span',class_='poemAuthor')
titleIndents = soup.find_all('div',class_='titleIndent')
id = soup.find_all('div',class_='_poem')
for i,title,author,titleIndent in zip(id,titles,authors,titleIndents):
    poemid = i.get('id')

    pattern = r"\d+"
    match = re.search(pattern, poemid)

    # 打印提取的数字
    if match:
        num = match.group()


        con = soup.select(f'#poem_content_{num}')
        for co in con:
            content = co.get_text()
        print(title.text,author.text,titleIndent.text,content)
# for title,author,titleIndent,text in zip(titles,authors,titleIndents):
#     print(title.text,author.text,titleIndent.text,)
#
#
# con = soup.select('#poem_content_23789')
# for co in con:
#     print(co.get_text())






