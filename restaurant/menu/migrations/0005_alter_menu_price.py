# Generated by Django 4.1.3 on 2022-11-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_rename_dish_desc_menu_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
