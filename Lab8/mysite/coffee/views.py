from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'coffee/index.html')

def products(request):
    mydata = coffee.objects.all()

    return render(request, 'coffee/products.html', context = {
        'allcoffee': mydata
    })

def productsAbout(request):
    is_id = request.GET['id']
    is_coffee = coffee.objects.get(id = is_id)

    return render(request, 'coffee/product_about.html', context = {
        'is_coffee': is_coffee
    })

def store(request):
    return render(request, 'coffee/store.html')