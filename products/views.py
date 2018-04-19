from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Product
from django.utils import timezone

@login_required(login_url="/login")
def home(request):
    products = Product.objects
    return render(request, 'products/home.html' , {'products':products})


@login_required(login_url="/login")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.POST['creator']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.image = request.FILES['image']

            product.pub_date = timezone.datetime.now()
            product.hunter = request.POST['creator']
            product.supporter = request.POST['creator']
            product.numbersupp = 1
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error' : 'All fields are required'})

    else:
        return render(request, 'products/create.html' )
"""
@login_required(login_url="/login")
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html',  {'product': product} )
"""
@login_required(login_url="/login")
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        if request.POST['supporter']:
            product.supporter += ', ' + request.POST['supporter']
            product.numbersupp += 1
            product.save()
            return  redirect( '/products/' + str(product.id),{'product': product, 'error' : 'Danke für deine Hilfe'+product.supporter})
        else:
            return render(request, 'products/detail.html', {'error' : 'bitte fülle alle Felder aus'})
    return render(request, 'products/detail.html', {'product': product, 'error' : 'Debug well'} )


"""@login_required(login_url="/login")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
    return redirect('/products/' + str(product.id))
"""
@login_required(login_url="/login")
def support(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        if request.POST['supporter']:
            product.supporter += ', ' + request.POST['supporter']
            product.numbersupp += 1
            product.save()
            return render(request, 'products/detail.html', {'product': product})
        else:
            return render(request, 'products/detail.html', {'error' : 'This shouldnet happen1'})
    return render(request, 'products/detail.html', {'error' : 'This shouldnet happen2'})
