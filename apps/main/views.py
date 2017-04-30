from django.shortcuts import render
from .models import Product
def index(request):
    return render(request, 'main/index.html')

def load_product(request, id):
    product = Product.objects.get(id = id)
    context = {
    'product': product
    }
    return render(request, 'main/load_product.html', context)
