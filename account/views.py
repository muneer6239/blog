from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration Successful")
            return render(request,'index.html')
        else:
            messages.error(request, "Please enter correct details as per requested format")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})

def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_authenticated:
                    return redirect('blogs')
                else:
                    return redirect('loginUser') 
            else:
                messages.error(request, "Invalid credentials or account not found")
                return redirect('loginUser')   
    else:
        form = LoginForm()
        if request.user.is_authenticated:
                return redirect('blogs')
        else:
            return render(request, 'login.html', {'form':form})

def logoutUser(request):
    messages.success(request, "Logout Successfully")
    logout(request)
    return redirect('index')

    
