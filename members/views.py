from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.core.cache import cache
pending_url={}
def index(r,key_id ):
    key_id=key_id.replace('11','/')
    k=''
    value = cache.get(key_id)
    if value is None:
        print('fetch')
        k=requests.get('https://'+key_id)  
        cache.set(key_id,k.text)
    return HttpResponse(cache.get(key_id))
    print('here ?')
def invalidate(r):
    cache.clear()
    return HttpResponse('Invalidated')
def invalidate_specific(r,key):
    key=key.replace('11','/')
    k=requests.get('https://'+key)  
    cache.set(key,k.text)
    return HttpResponse(cache.get(key))
def health(r):
    return HttpResponse('ok')


