from django.contrib import admin
from django.urls import path, include
from form2 import views

urlpatterns = [
    path('form2/', views.home, name="home")
]