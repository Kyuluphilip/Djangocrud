
from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.registration, name='registration'),
    path('registerpage/', views.mypage, name='myregisterpage'),
    path('',views.home, name='myhome'),
    path('home',views.home, name='myhome'),
    path('base', views.base, name='mybase'),
    path('login', views.login, name='mylogin'),
    path('products', views.products, name='myproducts'),
    path('courses', views.courses, name='mycourses'),
   # path('updates', views.courses, name='myupdates'),
    path('dashboard',views.dashboard, name='mydashboard'),

   # path('adduser', views.adduser, name='addinguser'),
    path('addstudent', views.addstudent, name='addingstudent'),
    path('editstudent/<id>', views.editstudent, name='editstudent'),
    path('updatestudent/<id>', views.updatestudent, name='updatestudent'),
    path('deletestudent/<id>', views.deletestudent, name='deletestudent'),
  #  path('pay',)


























]





























