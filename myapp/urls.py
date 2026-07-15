from django.urls import path
from .views import *
urlpatterns=[
    path('',indexview,name='index'),
    path('userlogin/',log,name='userlogin'),
    path('logout/',logoutview,name='logout'),
    path('loginpageaction/',loginview,name='loginaction'),
    path('register/',registerview,name='register'),
    path('about/',about_view,name='aview'),
    path('contact/',contact_view,name='cview'),
    path('help/',help_view,name='hview'),
    path('studentdashboard/',stdash,name='studentdashboard'),
    path('facultydashboard/',fcdash,name='facultydashboard'),
    path('facultylogin/',fclog,name='facultylogin'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('course/<int:course_id>/enroll/', enroll_course, name='enroll_course'),
    path('course/<int:course_id>/faculty/add-content/', faculty_add_content, name='faculty_add_content'),

    path('c1/',viewc1,name='c1'),
    path('c2/',viewc1,name='c2'),
    path('c3/',viewc1,name='c3'),
    path('c4/',viewc1,name='c4'),
    path('c5/',viewc1,name='c5'),
]