# Generated by Django 4.1.3 on 2022-11-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_menu_dish_category_remove_menu_dish_cuisine_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='dish_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='dish_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='dish_spice',
            new_name='spice',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='dish_price',
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, default=11, max_digits=5),
            preserve_default=False,
        ),
    ]
