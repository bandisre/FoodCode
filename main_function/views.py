from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Additive_list
import requests
import urllib.request
import json
import http.client
import mimetypes
import json

from django.http import JsonResponse
from django.core import serializers
from .Barcodereader import barcode_reader_camera



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
    ingre = ingre.replace('(', ',', ingre.count('('))
    ingre = ingre.replace(')', '', ingre.count(')'))
    ingre1 = [str(g) for g in ingre.split(',')]
   
    LofList = len(ingre1)
    Loftoxic = len(toxic)
   
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
    i = 0
    # k = 0
    
    # lenharmful = len(harmfulIngredients)
    # print(lenharmful)
    # while k < lenharmful:
    #     print(harmfulIngredients[k])
    #     k = k+1
    i = 0
    for ingredient in ingre1:
        if Additive_list.objects.filter(name__icontains = ingredient):
            harmfulIngredients.append(ingredient) 
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
    list_temp = [harmfulIngredients, productname, imageurl]
    print(list_temp)
    return list_temp


  #print("INGREDIENTS:", ingredients0, "PRODUCT NAME:", productname, "IMAGE URL:", imageurl)

# if __name__ == '__main__':
#     barcode = '028400642033'
#     ingredients_api(barcode)

class Search(TemplateView): 
    # url = 'https://api.barcodelookup.com/v2/products?barcode=072250011372&formatted=y&key=' + "ax4xj589yc5wpquahyp749dkfi4jhm"
    # # response = requests.get(url)
    # with urllib.request.urlopen(url) as url:
    #     data = json.loads(url.read().decode())
    # ingredients = ingredient_sort(data)
    template_name = 'main_function/search.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # url = 'https://api.barcodelookup.com/v2/products?barcode=072250011372&formatted=y&key=' + "ax4xj589yc5wpquahyp749dkfi4jhm"
        # with urllib.request.urlopen(url) as url:
        #     data = json.loads(url.read().decode())
        # returned_context = ingredient_sort(data)
        # ingredients = returned_context[0]


        ingredient_list_models = []
        ingredients = []
        if ingredients:
            for ingredient in ingredients:
                if Additive_list.objects.filter(name__icontains=ingredient):
                    ingredient_ = Additive_list.objects.filter(name__icontains=ingredient).all()
                    ingredient_list_models.append(ingredient_)
        context['ingredient_list_model'] = ingredient_list_models
        context['image'] = 'https://images.barcodelookup.com/2755/27556319-1.jpg'
        context['product_name'] = 'Cuisine Camino Organic Cocoa Powder'
     
        return context

class LandingPage(TemplateView):
    template_name = 'main_function/landing_page.html'
    
class Search_ajax(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            if request.POST.get("camera_button"):
                barcode_number = barcode_reader_camera()
                # print(barcode_number)
            if request.POST.get('barcode'):
                barcode_number = request.POST.get('barcode')
            # print(barcode_number)
            ingredient_list_model = []
            context_data =  ingredients_api(barcode_number)
            # print(context_data[0])
            # ingredients = context_data[0]
            # if ingredients:
            #     for ingredient in ingredients:
            #         if Additive_list.objects.filter(name__icontains=ingredient):
            #             ingredient_ = Additive_list.objects.filter(name__icontains=ingredient).all()
            #             name_ = ingredient_.name
            #             description = ingredient_.description
            #             pk = ingredient_.pk
            #             ingredient_list_model.append((name_, description, pk))
            context_data = [0, ['Wonder Bread'] ,['https://static.openfoodfacts.org/images/products/007/225/001/1372/front_en.10.400.jpg']]
            ingredient_list_model = [('Unenriched Wheat Flour', "Used in many snack foods. A refined starch that is made from toxic ingredients.", 20),
             ('High Fructose Corn Syrup', 'A sweetener made from corn starch. Made from genetically-modified corn. Causes obesity, diabetes, heart problems, arthritis and insulin resistance.', 54), 
             ('Soybean Oil', 'Unhealthy vegetable oil common in store products', 11)]
            print(ingredient_list_model)

            # serialized_qs = serializers.serialize('json', ingredient_list_models)
            # data = {"queryset" : serialized_qs}
            # data = []
            # data.append({'ingredients': ingredient_list_models})
            # print(data)
            return JsonResponse({'harmful_ingredients': ingredient_list_model, 'image_url': context_data[2], 'product_name': context_data[1], 'barcode': barcode_number}, status=200)
        print(False)
        return False


        



