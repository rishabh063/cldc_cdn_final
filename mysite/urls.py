from django.contrib import admin
from django.urls import path
from members import views 
from members import website
urlpatterns = [
   path('query/<str:key_id>/', views.index, name='index'),
   path('Forcedinvalidate/',views.invalidate, name='invalidate'),
   path('invalidate/<str:key>/',views.invalidate_specific, name='invalidate_specific'),
   path('health/',views.health, name='health'),
   path('website/' ,website.content , name='content' ),
   path('start_cdn/' ,website.start_cdn , name='start_cdn'),
   path('close_cdn/' ,website.close_cdn , name='close_cdn')
]
