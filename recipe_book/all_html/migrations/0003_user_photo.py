# Generated by Django 4.2.7 on 2023-11-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_remove_ingredient_category_recipe_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=None, upload_to='media/user_images'),
            preserve_default=False,
        ),
    ]
