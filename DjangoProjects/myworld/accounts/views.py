from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render , redirect
# Create your views her
from .forms import CreatUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account was created for ' + user)
            return redirect('loginPage')
    context = {
        'form': form 
    }
    return render(request, 'register.html',context)


def loginPage(request):
    if request.method  == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)
            return redirect('index')
    
    return render(request,'login.html')