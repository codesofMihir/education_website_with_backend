from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.
def indexview(request):
    return render(request,'pages\index.html')
@csrf_exempt
def registerview(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')

    if password!=confirmpassword:
        return redirect(request, "register")
    user=User.objects.filter(Username=username)
    if user.exists():
        messages.error(request,"username already taken")
        return redirect('register')

    createuser=User.objects.create_user(username=username,email=email,contact=contact,password=password)
   
    createuser.save()
    return redirect('userlogin')

def loginview(request):
    if request.method=='POST':
        Username=request.POST.get('username')
        password=request.POST.get('password')

    if not User.objects.filter(Username= Username).exists():
        messages.error(request,'Invalid username')
        return redirect('register')

    user=authenticate(username=Username,password=password)

    if user is None:
        messages.error(request,'Invalid password')
        return redirect('userlogin')


    else:
        login(user)
        return render('index')

    return render('index')

    



def log(request):
    return render(request,'pages/userlogin.html')

def rlog(request):
    return render(request,'pages/register.html')

def stdash(request):
    return render(request,'pages/studentdashboard.html')

def fcdash(request):
    return render(request,'pages/facultydashboard.html')
def fclog(request):
    return render(request,'pages/facultylogin.html')

def viewc1(request):
    return render(request,'c1.html')
def viewc2(request):
    return render(request,'c2.html')
def viewc3(request):
    return render(request,'c3.html')
def viewc4(request):
    return render(request,'c4.html')
def viewc5(request):
    return render(request,'c5.html')