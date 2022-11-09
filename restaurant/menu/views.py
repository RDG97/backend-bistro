from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Menu
from django.db import models
from .models import Category
# Create your views here.
def get_menu(request):
    data = list(Menu.objects.values())
    return JsonResponse({ 'data': data })

def get_all(request):
    data = list(Menu.objects.values())
    print(data)
    return JsonResponse({ 'data': data })