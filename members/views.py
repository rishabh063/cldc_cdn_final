from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.core.cache import cache
import gc
def index(r,key_id ):
    activate = cache.get('active')
    if activate!=1:
        return HttpResponse('CDN Not Active')
    key_id=key_id.replace('11','/')
    k=''
    value = cache.get(key_id)
    if value is None:
        k=requests.get('https://'+key_id)  
        cache.set(key_id,k.text)
    gc.collect()
    return HttpResponse(cache.get(key_id))
def invalidate(r):
    cache.clear()
    gc.collect()
    return HttpResponse('Invalidated')
def invalidate_specific(r,key):
    key=key.replace('11','/')
    k=requests.get('https://'+key)  
    cache.set(key,k.text)
    gc.collect()
    return HttpResponse(cache.get(key))
def health(r):
    gc.collect()
    return HttpResponse('ok')


