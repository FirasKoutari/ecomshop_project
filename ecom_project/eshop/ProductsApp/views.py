from django.shortcuts import render

# Create your views here.
def detail(request):
    return render(request,'detail.html')
def shop(request):
    return render(request,'shop.html')