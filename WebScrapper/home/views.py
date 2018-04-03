from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

# import tkinter as tk
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import requests, bs4

def scrap(param):
    prod = []
    products_list = []
    prices_list = []
    while(len(prod)==0):
        res = requests.get('https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}'.format(param))
        bs = bs4.BeautifulSoup(res.text,'html.parser')
        # print(len(res.text))
        # print(res.text[:100])
        prod = bs.select("h2")
        price = bs.select(".s-price")
        # print(len(prod))
        try:
            for i in range(len(price)):
                products_list.append(prod[i].getText())
                prices_list.append(price[i].getText())
        except IndexError:
            print("No result found!!!")
            break

        for i in range(len(products_list)):
            print(products_list[i],"-->",prices_list[i])

def index(request):
    form = forms.FormName()
    my_dict = {'insert_me':"Now I am coming from first_app/index.html!"
                ,'forms':form}
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation successfull")
            scrap(form.cleaned_data['search'])

    return render(request,'home/main.html',context=my_dict)
