from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import pdb

# Create your views here.
def login_user(request):
    if request.method == "POST":        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Impossible de vous authentifier, essayez à nouveau."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Vous avez été déconnecté avec succès."))
    return redirect('home')

def register_user(request):
    print("A")
    print(request.method)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        emailAddress = request.POST["emailAddress"]
        user = User.objects.create_user(username, emailAddress, password)
        user.save()
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        print(emailAddress)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, ("Vous vous êtes inscrit avec succès"))
            return redirect('home')
        else:
            messages.success(request, ("Impossible de vous inscrire, essayez à nouveau."))
            return redirect('register')
    else:        
        return render(request, 'register.html', {})

