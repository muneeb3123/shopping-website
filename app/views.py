from django.shortcuts import render

from django.contrib.auth.models import User 
from django import forms
from django.contrib.auth import authenticate,login,logout
from app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from app.models import products


def result(request):
    
    Moving=moving.objects.all()
    Main=main.objects.all()
    Selling=selling.objects.all()
    Feature=feature.objects.all()
    Banner1=banner1.objects.all()
    Feature1=feature1.objects.all()
    Recommended1=recommended1.objects.all()
    Banner3=banner3.objects.all()
    Brand=brand.objects.all()
    Banner4=banner4.objects.all()
    Banner5=banner5.objects.all()
    Banner6=banner6.objects.all()
    Product=products.objects.all()
    Banner=banner.objects.all().order_by("-id")[:3]
    Slider=slider.objects.all().order_by("-id")[:3]
    return render(request,'base.html',locals())

def product_details(request,slug):
    Product=products.objects.get(product_slug=slug)
    
    return render(request,"product-details.html",locals())

def my_account(request):
    return render(request,"my-account.html")





def my_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            
            return HttpResponseRedirect('/')
        else:
             msg=messages.error(request,"PASSWORD OR USERNAME IS WRONG!!")
             return render(request,"my-account.html",locals())

    return render(request,"my-account.html")

def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url="account")
def my_cart(request):
    return render(request,"cart.html")

@login_required(login_url="account")
def add_cart(request,id):
    cart=Cart(request)
    Product=products.objects.get(id=id)
    cart.add(product=Product)
    return HttpResponseRedirect("/")

@login_required(login_url="account")
def remove_cart(request,id):
    cart = Cart(request)
    Product = products.objects.get(id=id)
    cart.remove(Product)
    return HttpResponseRedirect("/cart_user/")

@login_required(login_url="account")
def item_increment(request,id):
    cart = Cart(request)
    Product = products.objects.get(id=id)
    cart.add(product=Product)
    return HttpResponseRedirect("/cart_user/")


@login_required(login_url="account")
def item_decrement(request,id):
    cart = Cart(request)
    Product = products.objects.get(id=id)
    cart.decrement(product=Product)
    return HttpResponseRedirect("/cart_user/")

@login_required(login_url="account")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponseRedirect("/cart_user/")
    
@login_required(login_url="account")
def check_out(request):
    return render(request,"checkout.html")

def Check_user(request):
    if request.method=="GET":
        username=request.GET['username']
        user=User.objects.filter(username=username)
        if(len(user)==1):
            return HttpResponse("EXIST")
        else:
            return HttpResponse("NOT EXIST")

def Add_user(request):
    if request.method=="GET":
        
         username=request.GET['username']
         password=request.GET['password']
         email=request.GET['email']
         user=User.objects.filter(username=username)
         if(len(user)==1):
          
          return HttpResponse("NOT SAVE")
         else:
            print("CHECK")
            user=User(username=username,email=email,)
            user.set_password(password)
            user.save()
            return HttpResponse("SAVE")


    