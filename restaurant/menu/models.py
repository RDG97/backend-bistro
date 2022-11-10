from django.db import models
from django.db.models import IntegerField, Model, ForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=15)

class Cuisine(models.Model):
    type = models.CharField(max_length=15)

class Menu(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=150)
    price = models.FloatField(null = True)
    spice = models.IntegerField(
                            default=1,
                            validators=[
                                MaxValueValidator(5),
                                MinValueValidator(1)
                            ])
    dish_category = ForeignKey(Category, on_delete=models.CASCADE,)
    dish_cuisine = ForeignKey(Cuisine, on_delete=models.CASCADE,)

    def json(self):
        return {
            'title': self.name,
            'description': self.desc,
            'price': self.price,
            'cuisine': {
                'title': self.dish_cuisine.type
            },
            'category': {
                'title': self.dish_category.type
            }}
    def __str__(self):
        return f"NAME: {self.name} DESCRIPTION: {self.desc}"