# %%
from selenium import webdriver

browser = webdriver.Chrome(executable_path="./chrome_driver/chromedriver.exe")
# %%
browser.get("https://hiskio.com/courses/527/about")
browser.page_source

browser.quit()
# %%
