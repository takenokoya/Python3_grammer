from bs4 import BeautifulSoup
import urllib.request as request


url = 'https://su-gi-rx.com/2018/03/28/text-mining-2/'

# urlopen()でデータを取得
res = request.urlopen(url)

# BeautifulSoup()で解析
soup = BeautifulSoup(res, 'html.parser')

# 任意のデータを抽出
title1 = soup.find('h1').string
print('title = ', title1)

p_list = soup.find_all('p')

for p in p_list:
    print(p.get_text())
