from django.urls import path
from .views import *
urlpatterns=[
    path('',indexview,name='index'),
    path('userlogin/',log,name='userlogin'),
    path('register/',rlog,name='register' ),
    path('studentdashboard/',stdash,name='studentdashboard'),
    path('facultydashboard/',fcdash,name='facultydashboard'),
    path('facultylogin/',fclog,name='facultylogin'),
]