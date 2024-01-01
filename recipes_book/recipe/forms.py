from django import forms
from django.forms import ModelForm

from .models import Recipe, Ingredient, Instruction, Image, Tag, Category, CookingTime, Author


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'images', 'tags', 'categories', 'cooking_times', 'authors']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'ingredients': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'instructions': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'images': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'cooking_times': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
            'images': 'Images',
            'tags': 'Tags',
            'categories': 'Categories',
            'cooking_times': 'Cooking Times',
            'author': 'Author',
        }
        help_texts = {
            'name': 'Enter the title of the recipe.',
            'description': 'Enter the description of the recipe.',
            'ingredients': 'Select the ingredients of the recipe.',
            'instructions': 'Select the instructions of the recipe.',
            'images': 'Select the images of the recipe.',
            'tags': 'Select the tags of the recipe.',
            'categories': 'Select the categories of the recipe.',
            'cooking_times': 'Select the cooking times of the recipe.',
            'author': 'Select the author of the recipe.',
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'quantity': 'Quantity',
            'unit': 'Unit',
        }
        help_texts = {
            'name': 'Enter the name of the ingredient.',
            'quantity': 'Enter the quantity of the ingredient.',
            'unit': 'Enter the unit of the ingredient.',
        }


class InstructionForm(ModelForm):
    class Meta:
        model = Instruction
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'description': 'Description',
        }
        help_texts = {
            'description': 'Enter the description of the instruction.',
        }


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'image': 'Image',
        }
        help_texts = {
            'image': 'Select the image of the recipe.',
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
        }
        help_texts = {
            'name': 'Enter the name of the tag.',
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
        }
        help_texts = {
            'name': 'Enter the name of the category.',
        }


class CookingTimeForm(ModelForm):
    class Meta:
        model = CookingTime
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
        }
        help_texts = {
            'name': 'Enter the name of the cooking time.',
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
        }
        help_texts = {
            'name': 'Enter the name of the author.',
        }






