from django.shortcuts import render
from ProductsApp.models import Product
def index(request):
    prod = Product.objects.all()
    return render(request,'index.html',{'prod': prod})
def contact(request):
    return render(request,'contact.html')
# Create your views here.
