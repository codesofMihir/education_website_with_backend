from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def explore_view(request):
    return render(request, 'userlogin.html')

def about_view(request):
    return render(request,'pages/about.html')
def help_view(request):
    return render(request,'pages/help.html')
@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        print(name,email,subject,message)

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        messages.success(request, 'Your message has been submitted successfully.')
        return redirect('cview')

    return render(request, 'pages/contact.html')

# Create your views here.
def indexview(request):
    #  scroll_banned = False
    # form = AuthenticationForm()

    # # If user is a guest, activate the scroll ban overlay
    # if not request.user.is_authenticated:
    #     scroll_banned = True
    course=Courses.objects.all()
    context={
        'coursedata':course
    }
        

    

    return render(request,'pages\index.html' , context)


@csrf_exempt
def registerview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password != confirmpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        createuser = User.objects.create_user(username=username, email=email, password=password)
        createuser.save()
        return redirect('userlogin')

    return render(request, 'pages/register.html')

@csrf_exempt
def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('userlogin')

        login(request, user)
        messages.success(request,'login successful')
        return redirect('index')

    return render(request, 'pages/userlogin.html')

def course_detail(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    return render(request, 'pages/coursedetail.html', {
        'course': course,
        'is_enrolled': is_enrolled,
    })
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    if request.method == 'POST':
        Enrollment.objects.get_or_create(student=request.user, course=course)
        messages.success(request, f'Enrolled in {course.product_name}')
    return redirect('course_detail', course_id=course.id)


def logoutview(request):
    logout(request)
    return redirect('index')
    



def log(request):
    return render(request,'pages/userlogin.html')

def rlog(request):
    return render(request,'pages/register.html')

@login_required
def stdash(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related('course')
    return render(request, 'pages/studentdashboard.html', {
        'enrollments': enrollments,
    })

def fcdash(request):
    return render(request,'pages/facultydashboard.html')
def fclog(request):
    return render(request,'pages/facultylogin.html')

def viewc1(request):
    return render(request,'pages/c1.html')
def viewc2(request):
    return render(request,'pages/c2.html')
def viewc3(request):
    return render(request,'pages/c3.html')
def viewc4(request):
    return render(request,'pages/c4.html')
def viewc5(request):
    return render(request,'pages/c5.html')