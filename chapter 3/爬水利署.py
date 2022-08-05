# %%
import requests

r = requests.get("https://fhyv.wra.gov.tw/FhyWeb/v1/Api/Reservoir/Visual?$format=JSON")
response = r.json()

response
# %%
