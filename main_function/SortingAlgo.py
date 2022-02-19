
#ingredient_list = "['Unbleached Enriched Flour (wheat Flour', 'Malted Barley Flour', 'Niacin', 'Reduced Iron', 'Thiamin Mononitrate', 'Riboflavin', 'Folic Acid)', 'Water', 'High Fructose Corn Syrup', 'Yeast', 'Contains 2% Or Less Of The Each Of The Following: Calcium Carbonate', 'Soybean Oil', 'Wheat Gluten', 'Salt', 'Dough Conditioners (contains One Or More Of The Following: Sodium Stearoyl Lactylate', 'Calcium Stearoyl Lactylate', 'Monoglycerides', 'Mono- And Diglycerides', 'Distilled Monoglycerides', 'Calcium Peroxide', 'Calcium Iodate', 'Datem', 'Ethoxylated Mono- And Diglycerides', 'Enzymes', 'Ascorbic Acid)', 'Vinegar', 'Monocalcium Phosphate', 'Yeast Extract', 'Modified Corn Starch', 'Sucrose', 'Sugar', 'Soy Lecithin', 'Cholecalciferol (vitamin D3)', 'Soy Flour', 'Ammonium Sulfate', 'Calcium Sulfate', 'Calcium Propionate (to Retard Spoilage).']"
#toxic = ['Unbleached Enriched Flour', 'High Fructose Corn Syrup', 'Soybean Oil']
import http.client
import mimetypes
import json
from .models import Additive_list

# def ingredient_sort(data):
#     harmfulIngredients = []
#     EmptyListList = [""]
#     data_ingredients = data['products'][0]['ingredients']
#     product_name = data['products'][0]['product_name']
#     image_url = data['products'][0]['images']
#     EmptyList = ""
#     if data_ingredients == EmptyList:
#         harmfulIngredients.append(EmptyListList)
#         return False
#     characters = ['(', ')']
#     for character in characters:
#         data_ingredients = data_ingredients.replace(character,"")
#     data_ingredients = [str(g) for g in data_ingredients.split(',')]
#     LofList = len(data_ingredients)
#     i = 0
#     while LofList > i:
#         if Additive_list.objects.filter(name__icontains = data_ingredients[i]):
#             harmfulIngredients.append(data_ingredients[i]) 
#             i = i+1
#         else:
#             i = i+1
#     temp_list = [harmfulIngredients, product_name, image_url]
#     return temp_list

# def ingredients_api(barcode):
#     barcode = barcode
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
#             ingredients = json_obj['product']
    
#     conn.request("GET", "/api/v0/product_name/" + barcode + ".json?fields=product_name", payload, headers)
#     res = conn.getresponse()
#     data = res.read().decode("utf-8")
#     json_obj = json.loads(data)
#     for key in json_obj:
#         if (key == 'product'):
#             productname = json_obj['product']

#     conn.request("GET", "/api/v0/product_name/" + bracode + ".json?fields=image_url", payload, headers)
#     res = conn.getresponse()
#     data = res.read().decode("utf-8")
#     json_obj = json.loads(data)
#     for key in json_obj:
#         if (key == 'product'):
#             imageurl = json_obj['product']
    

    

    

# def ingredient_sort_local(data):
#     harmfulIngredients = []
#     EmptyListList = [""]
#     data_ingredients = data['products'][0]['ingredients']
#     product_name = data['products'][0]['product_name']
#     image_url = data['products'][0]['images']
#     EmptyList = ""
#     if data_ingredients == EmptyList:
#         harmfulIngredients.append(EmptyListList)
#         return False
#     characters = ['(', ')']
#     for character in characters:
#         data_ingredients = data_ingredients.replace(character,"")
#     data_ingredients = [str(g) for g in data_ingredients.split(',')]
#     LofList = len(data_ingredients)
#     i = 0
#     while LofList > i:
#         if data_ingredients[i] in toxic:
#             harmfulIngredients.append(data_ingredients[i]) 
#             i = i+1
#         else:
#             i = i+1
#     temp_list = [harmfulIngredients, product_name, image_url]
#     return temp_list
      
# if __name__ == '__main__':
#     ingredient_sort_local(ingredient_list)


import http.client
import mimetypes
import json
import re

def ingredients_api(barcode):
    toxic = ['Unbleached Enriched Flour', 'High Fructose Corn Syrup', 'Soybean Oil', 'sugar', 'salt']
    harmfulIngredients = []
    conn = http.client.HTTPSConnection("world.openfoodfacts.org")
    payload = ''
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    conn.request("GET", "/api/v0/product_name/" + barcode + ".json?fields=ingredients_text_en", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_obj = json.loads(data)
    for key in json_obj:
        if (key == 'product'):
            ingredients0 = json_obj['product']

    for key in ingredients0:
        ingre = ingredients0[key]
    print(ingre)
    ingre = ingre.replace('(', ',', ingre.count('('))
    ingre = ingre.replace(')', '', ingre.count(')'))
    ingre1 = [str(g) for g in ingre.split(',')]
    LofList = len(ingre1)
    Loftoxic = len(toxic)
    print(LofList)
    print(Loftoxic)
    i = 0
    # while LofList < i:
    #     j=0
    #     while Loftoxic < j:
    #         if (ingre1[i] == toxic[j]):
    #             harmfulIngredients.append(ingre1[i]) 
    #         j = j+1
    #     i = i+1
    # for ingredient in ingre:
    #     if ingredient in toxic:
    #         harmfulIngredients.append(ingredient)
    # print(i)
    # #print(ingre)
    # lenlist = len(ingre)
    # i = 0
    # k = 0
    
    # lenharmful = len(harmfulIngredients)
    # print(lenharmful)
    # while k < lenharmful:
    #     print(harmfulIngredients[k])
    #     k = k+1

    while LofList > i:
        if Additive_list.objects.filter(name__icontains = ingres1[i]):
            harmfulIngredients.append(ingre1[i]) 
            i = i+1

    print(harmfulIngredients)
    conn.request("GET", "/api/v0/product_name/" + barcode + ".json?fields=product_name", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_obj = json.loads(data)
    for key in json_obj:
        if (key == 'product'):
            productname = json_obj['product']

    conn.request("GET", "/api/v0/product_name/" + barcode + ".json?fields=image_small_url", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_obj = json.loads(data)
    for key in json_obj:
        if (key == 'product'):
            imageurl = json_obj['product']

    #print("INGREDIENTS:", ingredients0, "PRODUCT NAME:", productname, "IMAGE URL:", imageurl)

if __name__ == '__main__':
    barcode = '028400642033'
    ingredients_api(barcode)