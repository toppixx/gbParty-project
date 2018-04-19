from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product

@login_required(login_url="/login")
def dieparty(request):
    products = Product.objects
    return render(request, 'party/dieparty.html')

@login_required(login_url="/login")
def history(request):
    return render(request, 'party/history.html')

@login_required(login_url="/login")
def todos(request):
    products = Product.objects
    return render(request, 'party/todos.html',{'products':products})

@login_required(login_url="/login")
def home(request):
    products = Product.objects
    return render(request, 'party/home.html',{'products':products})

def handler404(request):
    return render(request, 'error404.html')

def error404(request):
    return render(request, 'error404.html')
