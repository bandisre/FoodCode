import requests
import json
import urllib.request

url = "https://world.openfoodfacts.org/api/v0/product/072250011372"

payload = {}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data = payload)
data = response.text.encode('utf8')


with urllib.request.urlopen(url) as url:
    data=json.loads(url.read().decode())
print(data['product']['product_name_en_imported'])
# response = requests.get(url)
    # with urllib.request.urlopen(url) as url:
    #     data = json.loads(url.read().decode())
    # ingredients = ingredient_sort(data)