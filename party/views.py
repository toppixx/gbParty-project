from products.models import Product

from django.shortcuts import render, get_object_or_404

from products.models import Product
def home(request):
    products = Product.objects
    return render(request, 'party/home.html',{'products':products}
)

def handler404(request):
    return render(request, 'error404.html')
