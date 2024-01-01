from django import forms

from .models import Recipe, Ingredient, Category


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'image', 'ingredients', 'category', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ImageField(attrs={'class': 'form-control'}),
            'ingredients': forms.CheckboxSelectMultiple(),
            'category': forms.CheckboxSelectMultiple(),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }








