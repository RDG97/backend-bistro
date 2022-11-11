from django.contrib import admin
from .models import Menu
from .models import Category
from .models import Cuisine

# Register your models here.
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Cuisine)