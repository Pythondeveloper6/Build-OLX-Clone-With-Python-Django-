from django.shortcuts import render
from product.models import Product , Category
# Create your views here.

def home(request):
    
    all_category = Category.objects.all() 
    products = Product.objects.all()

    template = 'home.html'
    context = { 'all_category' : all_category , 'products' : products}

    return render(request , template , context)