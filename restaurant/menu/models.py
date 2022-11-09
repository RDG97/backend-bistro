from django.db import models
from django.db.models import IntegerField, Model, ManyToManyField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=15)

class Cuisine(models.Model):
    type = models.CharField(max_length=15)

class Menu(models.Model):
    dish_name = models.CharField(max_length=30)
    dish_desc = models.CharField(max_length=150)
    dish_price = models.PositiveIntegerField()
    dish_spice = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    dish_category = ManyToManyField(Category)
    dish_cuisine = ManyToManyField(Cuisine)