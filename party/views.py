from django.shortcuts import render
from products.models import Product

def home(request):
    return render(request, 'party/home.html')
