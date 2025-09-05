from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from myapp.models import *



def index(request):
    return render(request,'index.html')

@login_required(login_url="login_reg")
def accounts(request):
    return render(request,'accounts.html')
    # all_orders = CustomerOrder.objects.filter(user=request.user)
    # return render(request,"accounts.html",{"orders":all_orders})    

@login_required(login_url="login_reg")
def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')
def reservation(request):
    return render(request,'reservation.html')
def service(request):
    return render(request,'service.html')
def testimonial(request):
    return render(request,'testimonial.html')
def login_reg(request):
    return render(request,'login_reg.html')

def userReg(request):
    try : 
        if request.method=='POST':
            data = request.POST
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            u = User(username=username,email=email)
            u.set_password(password)
            u.save()
            return render(request,"login_reg.html",{"rmessage":"Registration successfully"})
    except Exception as e:
            return render(request,"login_reg.html",{"rerr":"Something went wrong"})


def userLogin(request):
    try : 
        if request.method=='POST':
            data = request.POST
            username = data.get("username")
            password = data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
            else:

                return render(request,"login_reg.html",{"lerr":"Invalid credentials"})

            # return render(request,"login_reg.html",{"message":"Registration success"})

    except Exception as e:
            return render(request,"login_reg.html",{"lerr":"Something went wrong"})
def userlogout(request):
    logout(request)
    return redirect("index")
        

    