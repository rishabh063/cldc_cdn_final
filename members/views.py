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
