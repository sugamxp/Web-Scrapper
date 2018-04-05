from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
# Create your views here.

# import tkinter as tk
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import requests, bs4
def scrapAmazon(param,t):
    prod = []
    products_list = []
    prices_list = []
    while(len(prod)==0):
        res = requests.get('https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}'.format(param))
        bs = bs4.BeautifulSoup(res.text,'html.parser')
        # print(len(res.text))
        # print(res.text[:100])
        prod = bs.select(".s-access-title")
        price = bs.select(".s-price")
        # print(len(prod))
        try:
            for i in range(len(price)):
                products_list.append(prod[i].getText()[:100] + "...")
                prices_list.append(price[i].getText())

        except IndexError:
            print("No result found!!!")
            break
        for i in range(len(products_list)):
            search_model = models.SearchResult.objects.get_or_create(query =t, name = products_list[i],price = prices_list[i])[0]
            search_model.save()
            print("<-----------Added to Database--------------->")
            print(products_list[i],"-->",prices_list[i])
# https://www.flipkart.com/search?q=mitv
def scrapFlipkart(param,t):
    print("In flipkart")
    prod = []
    products_list = []
    prices_list = []
    while(len(prod)==0):
        res = requests.get('https://www.flipkart.com/search?q={}'.format(param))
        bs = bs4.BeautifulSoup(res.text,'html.parser')
        print(len(res.text))
        print(res.text[:100])
        prod = bs.select("._3wU53n")
        price = list(set(bs.select("._1vC4OE")).intersection(set(bs.select("._2rQ-NK"))))
        print(len(prod))
        print(len(price))
        try:
            for i in range(len(price)):
                products_list.append(prod[i].getText()[:100] + "...")
                prices_list.append(price[i].getText())
        except IndexError:
            print("No result found!!!")
            break
        print(len(products_list),len(prices_list))
        for i in range(len(products_list)):
            search_m = models.SearchResultFlipkart.objects.get_or_create(queryF =t, nameF = products_list[i],priceF = prices_list[i])[0]
            search_m.save()
            print("<-----------Added to Database--------------->")
            print(products_list[i],"-->",prices_list[i])
        print("Done")
def index(request):
    form = forms.FormName()
    t = None
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation successfull")
            s = form.cleaned_data['search']
            t = models.Search.objects.get_or_create(search_value = s)[0]
            t.save()
            scrapAmazon(s,t)
            scrapFlipkart(s,t)
    if t==None:
        search_result = []
        search_result_F = []
    print(t)

    search_result = models.SearchResult.objects.filter(query = t)
    search_result_F = models.SearchResultFlipkart.objects.filter(queryF = t)
    my_dict = {'insert_me':"Now I am coming from first_app/index.html!"
                ,'forms':form,
                'recordsA':search_result,
                'recordsF':search_result_F}
    return render(request,'home/main.html',context=my_dict)
# <div class="_1vC4OE_2rQ-NK">₹<!-- -->22,999</div>
