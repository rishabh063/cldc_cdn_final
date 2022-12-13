from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.core.cache import cache
from django.shortcuts import render
def content(r):
    value = cache.get('active')
    if value is None:
        return render(r , "index.html")
    elif value==0 :
        return render(r , "index.html")
    return HttpResponse('Site Not Active')
    # return render(r , "index.html")
def start_cdn(r):
    cache.set('active' , 1)
    return HttpResponse('cdn activated')
def close_cdn(r):
    cache.set('active' , 0)
    return HttpResponse('cdn Closed')

