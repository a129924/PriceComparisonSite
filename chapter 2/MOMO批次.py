# %%
import requests
from bs4 import BeautifulSoup

# %%
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
r = requests.get(
    f"https://m.momoshop.com.tw/search.momo?_advFirst=N&_advCp=N&curPage=1&searchType=1&authorNo=&cateLevel=-1&osm=Ad09&ent=k&searchKeyword=%E3%80%90Apple+%E8%98%8B%E6%9E%9C%E3%80%91iPhone+13+128G&_advThreeHours=N&_isFuzzy=0&_imgSH=fourCardType"    ,headers=headers)

soup = BeautifulSoup(r.text)
soup
# %%
items = soup.find("h3",class_="prdName")
# %%
