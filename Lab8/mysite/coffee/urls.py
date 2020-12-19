from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('products', products, name='products_url'),
    path('productsAbout', productsAbout, name='productsAbout_url'),
    path('store', store, name='store_url'),
]