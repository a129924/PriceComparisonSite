# %%
import requests
from bs4 import BeautifulSoup

# %%
r = requests.get(
    f"https://tw.buy.yahoo.com/search/product?p=Apple+iPhone+13+128G+5G%E6%89%8B%E6%A9%9F")

soup = BeautifulSoup(r.text)
soup
# %%
items = soup.find('div', class_='main') \
            .find('ul', class_='gridList') \
            .find_all('li', class_='BaseGridItem__grid___2wuJ7')

# %%
for item in items:
    print(item.find('span', class_="BaseGridItem__title___2HWui").text)
    print(item.find('em').text)
    print(item.find('a')['href'])

# %%
links = [item.find('a')['href'] for item in items]
links

# %%
products = []
for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.text)
    
    product = {}
    product['網址'] = link
    product['商品名稱'] = soup.find(
        'h1', class_='HeroInfo__title___57Yfg HeroInfo__textTooLong___BXk8j').text
    product['價錢'] = soup.find('div', class_='HeroInfo__mainPrice___1xP9H').text
    product['優惠'] = soup.find(
        'div', class_='InfoCell__cellContentWrap___2yfZW').text
    products.append(product)

products
# %%
