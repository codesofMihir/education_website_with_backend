from django.shortcuts import render

# Create your views here.
def indexview(request):
    return render(request,'pages\index.html')

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