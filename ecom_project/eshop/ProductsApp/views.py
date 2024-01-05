from django.shortcuts import render
from .models import Product
# Create your views here.
def detail(request):
    return render(request,'detail.html')


def shop(request):
    prod = Product.objects.all()
    return render(request,'shop.html', {'prod': prod})
