import requests
from bs4 import BeautifulSoup

url = 'https://fanqienovel.com/reader/7276663560427471412'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
print(response.text)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

chapter_titles = [title.text for title in soup.find_all('h1', class_='chapter-title')]
contents = [p.text for p in soup.find_all('p', class_='chapter-content')]

with open('novel.txt', 'w', encoding='utf-8') as f:
    for title, content in zip(chapter_titles, contents):
        f.write(title + '\n')
        f.write(content + '\n\n')
