# %%
import requests
from bs4 import BeautifulSoup
# %% 爬YAHOO超級商城
url = f"https://tw.buy.yahoo.com/gdsale/Apple-iPhone-13-128G-5G%E6%89%8B%E6%A9%9F-9720962.html?from=pla&gg=0&co_servername=Pmax_211216&gclid=CjwKCAjwlqOXBhBqEiwA-hhitNAeFFInpWmgKLigAddrx1Tlj4jaHRqhGhjcyM2Cl4E11hTqNcYgxxoCjIkQAvD_BwE&gclsrc=aw.ds"
r = requests.get(url)
response = r.text
# %% 
soup = BeautifulSoup(response)
# %% 直接挑選到想要的物件
soup.find("h1",class_="HeroInfo__title___57Yfg HeroInfo__textTooLong___BXk8j")

# %% 利用 CSS Selector 作篩選
soup.select("h1[class*='HeroInfo__title___']")

# %% Regex(正則表達式) 作篩選
import re
reg = re.compile("HeroInfo__title___")
soup.find("h1",class_=reg)

# %% 搜尋價格
price = soup.find("div", class_="HeroInfo__mainPrice___1xP9H")
price.text
# %% 轉換純數字
float(price.text[1:].replace(",",""))

# %% 找尋優惠
discount = soup.find("span", class_="PromotionInfo__tagTitle___1-fEB")
discount.text

# %% 爬MOMO
url_momo = f"https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=9691172&osm=Ad09&utm_source=BD_looca&utm_medium=google_pla&utm_content=bn&gclid=CjwKCAjwlqOXBhBqEiwA-hhitOTHyY82Kjw19K8Hejk46Y2O8DLtqkO_-MbZQV9Mxu14z0-CCX_DbhoCR7wQAvD_BwE"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
r = requests.get(url_momo, headers=headers)

soup = BeautifulSoup(r.text)
soup

# %% 找尋商品名稱
product_name = soup.find("p", id="osmGoodsName")
product_name.text
# %% 找尋價格
price = soup.find("li", class_="special").span
price.text
# %% 轉換純數字
float(price.text.replace(",",""))
# %% 找尋優惠
discount = soup.find("li", id="promoThDesc").span
discount.text.split('\n')[0]
# %%
