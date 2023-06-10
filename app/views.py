from django.shortcuts import render,redirect
from .models import Recipe
from .forms import *
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from myapp.models import User
# Create your views here.

@login_required(login_url='login')
def add_recipe(request):
    if request.method =="POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RecipeForm()
    return render(request,'index.html',{'form':form})

@login_required(login_url='login')
def home(request):
    recipes = Recipe.objects.all()
    return render(request,'home.html',{'recipes':recipes})

@login_required(login_url='login')
def delete(request,id):
    if request.method =="POST":
        pi = Recipe.objects.get(pk=id)
        pi.delete()
        return redirect('/')
  
@login_required(login_url='login')  
def update(request,id):
    if request.method =="POST":
        pi = Recipe.objects.get(pk=id)
        fm = RecipeForm(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
         pi = Recipe.objects.get(pk=id)
         fm = RecipeForm(instance=pi)
    return render(request,'update.html',{'form':fm})


def user_signup(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        cpassowrd = request.POST['confirm_passowrd']
        
        if password == cpassowrd:
            
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email Already Exists..")
                return redirect('signup')
            
            else:
                user = User.objects.create_user(email=email,password=password)
                user.save()
                messages.success(request,"Account Created Successfully...")
                return redirect('signup')
        else:
            messages.error(request,"Password Must be Same...")
            return redirect('signup')
    return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(request,email=email,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Invalid username/passowrd...")
            return redirect('login')
    return render(request,'login.html')

def user_logout(request):
     auth.logout(request)
     return redirect('login')