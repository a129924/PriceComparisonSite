# %%
import requests
from bs4 import BeautifulSoup

# %%
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
r = requests.get(
    f"https://m.momoshop.com.tw/search.momo?_advFirst=N&_advCp=N&curPage=1&searchType=1&authorNo=&cateLevel=-1&osm=Ad09&ent=k&searchKeyword=%E3%80%90Apple+%E8%98%8B%E6%9E%9C%E3%80%91iPhone+13+128G&_advThreeHours=N&_isFuzzy=0&_imgSH=fourCardType",headers=headers)

soup = BeautifulSoup(r.text)
soup
# %%
items = soup.find("h3",class_="prdName")
# %%
momo_base_url = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?"
links = [momo_base_url + item.a["href"].split("?")[1] for item in soup.find_all("li",class_="goodsItemLi")]
links
# %%

products = []
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

for link in links:
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.text)
    
    product = {}
    product["網址"] = link
    product["商品名稱"] = soup.find("div", class_="prdnoteArea").h3.text
    product["價錢"] = soup.find("ul",class_="prdPrice").find("li", class_="special").span.text
    product["優惠"] = soup.find("li", id="promoThDesc").span.text.split('\n')[0]
    
    products.append(product)
    
products
# %%
page = 5
keyword = "iPhone 13 128G"
links:list = []
momo_base_url = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?"

for page in range(1,page+1):
    url = f"https://m.momoshop.com.tw/search.momo?_advFirst=N&_advCp=N&curPage={page}&searchType=1&authorNo=&cateLevel=-1&osm=Ad09&ent=k&searchKeyword={keyword}&_advThreeHours=N&_isFuzzy=0&_imgSH=fourCardType"
    r = requests.get(url,headers=headers)

    soup = BeautifulSoup(r.text)
    
    for item in soup.find_all("li",class_="goodsItemLi"):
        links.append(momo_base_url + item.a["href"].split("?")[1])
        
links
# %%
products = []
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

for link in links:
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.text)
    
    product = {}
    product["網址"] = link
    product["商品名稱"] = soup.find("div", class_="prdnoteArea").h3.text
    product["價錢"] = soup.find("ul",class_="prdPrice").find("li", class_="special").span.text
    product["優惠"] = soup.find("li", id="promoThDesc").span.text.split('\n')[0]
    
    products.append(product)
    
products
# %%
