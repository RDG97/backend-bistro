from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.get_menu),
    path('allmenu/', views.get_all),
    path('test/', views.test)
]
