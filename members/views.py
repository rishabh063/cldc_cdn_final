from django.shortcuts import render
from django.http import HttpResponse
import requests
cache={}
def index(r,key_id ):
    key_id=key_id.replace('11','/')
    k=''
    if key_id not in cache:
        k=requests.get('https://'+key_id)        
        cache[key_id]=k.text
    return HttpResponse(cache[key_id])
def invalidate(r):
    global cache
    cache={}
    return HttpResponse('Invalidated')
def invalidate_specific(r,key):
    global cache
    key=key.replace('11','/')
    cache.pop(key, None)
    if key not in cache:
        k=requests.get('https://'+key)        
        cache[key]=k.text
    return HttpResponse(cache[key])