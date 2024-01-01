from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/user_images')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/')
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


