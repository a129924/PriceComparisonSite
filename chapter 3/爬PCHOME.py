# %%
import requests

r = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=Apple iPhone 13 128G&page=1&sort=sale/dc")

response = r.json()
print(response)
# %%
