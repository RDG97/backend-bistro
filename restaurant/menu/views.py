from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from .models import Menu
from django.db import models
from .models import Category
import json
# Create your views here.
def get_menu(request):
    data = list(Menu.objects.values())
    return JsonResponse({ 'data': data })

def get_all(request):
    data = [i.json() for i in Menu.objects.all()]
    return HttpResponse(json.dumps(data), content_type="application/json")