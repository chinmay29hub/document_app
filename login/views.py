from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "home.html") 
        else:
            messages.error(request, "Bad Credentials")
            return redirect('/login')

    return render(request, 'login.html')

def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(request, "your account has been successfully created")

        return redirect('/login')



    return render(request, 'register.html')

def Home(request):
    return render(request, 'home.html')

def Logout(request):
    logout(request)
    messages.success(request, "Logged Out Succesfully")
    return redirect('/login')