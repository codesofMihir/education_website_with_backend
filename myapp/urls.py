from django.urls import path
from .views import *
urlpatterns=[
    path('',indexview,name='index'),
    path('userlogin/',log,name='userlogin'),
    path('loginpageaction/',loginview,name='loginaction'),
    path('register/',registerview,name='register'),
    path('studentdashboard/',stdash,name='studentdashboard'),
    path('facultydashboard/',fcdash,name='facultydashboard'),
    path('facultylogin/',fclog,name='facultylogin'),
    path('cl/',viewc1,name='c1'),
    path('c2/',viewc1,name='c2'),
    path('c3/',viewc1,name='c3'),
    path('c4/',viewc1,name='c4'),
    path('c5/',viewc1,name='c5'),
]