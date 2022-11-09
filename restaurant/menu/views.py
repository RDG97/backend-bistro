from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Menu

# Create your views here.
def get_menu(request):
    data = list(Menu.objects.values())
    return JsonResponse({ 'data': data })