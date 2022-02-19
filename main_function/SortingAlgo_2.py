
from main_functions.models import Additive_list
import http.client
import mimetypes
import json
import re


# def ingredients_api(barcode):
#     toxic = ['Unbleached Enriched Flour', 'High Fructose Corn Syrup', 'Soybean Oil', 'sugar', 'salt']
#     harmfulIngredients = []
#     conn = http.client.HTTPSConnection("world.openfoodfacts.org")
#     payload = ''
#     headers = {
#     'Content-Type': 'application/x-www-form-urlencoded'
#     }

#     conn.request("GET", "/api/v0/product_name/" + barcode + ".json?fields=ingredients_text_en", payload, headers)
#     res = conn.getresponse()
#     data = res.read().decode("utf-8")
#     json_obj = json.loads(data)
#     for key in json_obj:
#         if (key == 'product'):
#             ingredients0 = json_obj['product']

#     for key in ingredients0:
#         ingre = ingredients0[key]
#     print(ingre)
#     ingre = ingre.replace('(', ',', ingre.count('('))
#     ingre = ingre.replace(')', '', ingre.count(')'))
#     ingre1 = [str(g) for g in ingre.split(',')]
#     LofList = len(ingre1)
#     Loftoxic = len(toxic)
#     print(LofList)
#     print(Loftoxic)
#     i = 0
#     # while LofList < i:
#     #     j=0
#     #     while Loftoxic < j:
#     #         if (ingre1[i] == toxic[j]):
#     #             harmfulIngredients.append(ingre1[i]) 
#     #         j = j+1
#     #     i = i+1
#     # for ingredient in ingre:
#     #     if ingredient in toxic:
#     #         harmfulIngredients.append(ingredient)
#     # print(i)
#     # #print(ingre)
#     # lenlist = len(ingre)
#     # i = 0
#     # k = 0
    
#     # lenharmful = len(harmfulIngredients)
#     # print(lenharmful)
#     # while k < lenharmful:
#     #     print(harmfulIngredients[k])
#     #     k = k+1

#     while LofList > i:
#         if Additive_list.objects.filter(name__icontains = ingres1[i]):
#             harmfulIngredients.append(ingre1[i]) 
#             i = i+1

#     print(harmfulIngredients)
#     conn.request("GET", "/api/v0/product_name/" + barcode + ".json?fields=product_name", payload, headers)
#     res = conn.getresponse()
#     data = res.read().decode("utf-8")
#     json_obj = json.loads(data)
#     for key in json_obj:
#         if (key == 'product'):
#             productname = json_obj['product']

#     conn.request("GET", "/api/v0/product_name/" + barcode + ".json?fields=image_small_url", payload, headers)
#     res = conn.getresponse()
#     data = res.read().decode("utf-8")
#     json_obj = json.loads(data)
#     for key in json_obj:
#         if (key == 'product'):
#             imageurl = json_obj['product']



# if __name__ == '__main__':
#     barcode = '028400642033'
#     ingredients_api(barcode)