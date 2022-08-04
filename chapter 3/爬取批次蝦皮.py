# %%
from selenium import webdriver
# %%
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup
import time

# %% 
browser = webdriver.Chrome(executable_path="./chrome_driver/chromedriver.exe")
browser.get(f"https://shopee.tw/search?keyword=apple%20iphone%2013%20128g")
browser.maximize_window() # 要把畫面放到最大 才能load到資料

for y in range(0, 10000, 500):
    browser.execute_script(f"window.scrollTo(0, {y})")
    print(y)
    time.sleep(0.5)

# %%
time.sleep(0.5)
source = browser.page_source
soup = BeautifulSoup(source)

# %%
links = []
for d in soup.find_all(class_='shopee-search-item-result__item'):
    links.append(d.a["href"])

# %%
browser.quit()
# %%
products = []
t = ''
for d in links[:2]:
    link = f"https://shopee.tw/{d}"
    browser.get(link)
    
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "attM6y")
        )
    )
    
    soup = BeautifulSoup(browser.page_source)
    
    product = {}
    product['網址'] = link
    t = product['商品名稱'] = soup.find("div",class_="flex flex-auto HLQqkk") \
        .find("div",class_="flex-auto flex-column imEX5V") \
        .find("div",class_="VCNVHn").span.text
        
    product['價錢'] = soup.find("div",class_="pmmxKx").text
    
    if soup.find("div",class_="lTuS3S"):
        product['優惠'] = soup.find("div",class_="lTuS3S").text
    products.append(product)
    
products
# %%
