# %%
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# %%
browser = webdriver.Chrome(executable_path="./chrome_driver/chromedriver.exe")

browser.get("https://shopee.tw/Apple-iPhone-13-128G-%E5%8E%9F%E5%BB%A0%E4%BF%9D%E5%9B%BA%E4%B8%80%E5%B9%B4-%E5%85%A8%E6%96%B0-%E7%8F%BE%E8%B2%A8-%E5%85%AC%E5%8F%B8%E8%B2%A8-%E5%BF%AB%E9%80%9F%E5%87%BA%E8%B2%A8-13-i13-6.1%E5%90%8B-Q%E5%93%A5-i.109729156.13174241915?sp_atk=b75fa997-b23e-437d-9b4c-e33455372834&xptdk=b75fa997-b23e-437d-9b4c-e33455372834")
source = browser.page_source
browser.quit()

soup = BeautifulSoup(source)
# %%
soup
# %% 取得產品名稱
soup.find("div",class_="flex flex-auto HLQqkk").find("div",class_="flex-auto flex-column imEX5V").find("div",class_="VCNVHn").span.text
# %% 取得產品價格
float(soup.find("div",class_="pmmxKx").text[1:].replace(",", ""))
# %% 取得商品優惠
soup.find("div",class_="lTuS3S").text

# %%
