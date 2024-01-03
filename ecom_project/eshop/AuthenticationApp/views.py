from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user khdawo')
                return redirect('login')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email deja khdawo')
                return redirect('login')

            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User created')
                return redirect('login')
        else:
            print('Passwords do not match')
            return redirect('/')


            

    return render(request, "logi.html")
