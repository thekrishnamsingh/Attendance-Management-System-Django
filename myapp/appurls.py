from django.contrib import admin
from django.urls import path,  include
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('registration/', views.registration, name='registration'),
    path('signin/',views.signin,name='login'),
    path('panel/',views.panel,name='panel'),
    path('mainpanel/',views.mainpanel,name='mainpanel'),
    path('signout/',views.singout,name='logout'),
    path('record/',views.record,name='record'),
    path('profile/',views.profile,name='profile'),
]
