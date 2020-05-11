# TODO: エラーがでてしまうので、要解消
import requests
from bs4 import BeautifulSoup


url = 'https://su-gi-rx.com'
images = []

soup = BeautifulSoup(requests.get(url).content, 'lxml')

for link in soup.find_all('img'):
    if link.get('src').endswith('.jpg'):
        images.append(link.get('src'))
    elif link.get('src').endswith('.png'):
        images.append(link.get('src'))

for target in images:
    res = requests.get(target)
    with open('img/' + target.split('/')[-1], 'wb') as f:
        f.write(res.content)

print('finish')