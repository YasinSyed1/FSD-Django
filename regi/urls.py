from django.contrib import admin
from django.urls import path, include
from regi import views

urlpatterns = [
    # path('new/', views.register, name="register"),
    path('form1/', views.home, name="home")
]