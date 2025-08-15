from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'featured_products': products.order_by('?')[:3]
    }
    return render(request, 'home.html', context)