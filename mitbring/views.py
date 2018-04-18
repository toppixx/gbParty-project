from django.shortcuts import render



def create(request):
    return render(request, 'products/create.html' )

def mitbring(request):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'mitbring/detail.html' )
