import logging
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Recipe, Ingredient, Category
from .forms import RecipeForm


# Create your views here.

def index(request):
    # фильтровать 5 последних добавленных рецептов
    context = {'recipes': Recipe.objects.all().filter().order_by('-id')[:5]}
    return render(request, 'recipe/index.html', context)


logger = logging.getLogger(__name__)


def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            ingredients = form.cleaned_data['ingredients']
            category = form.cleaned_data['category']
            user = form.cleaned_data['user']
            recipe = Recipe(name=name, description=description, image=image, ingredients=ingredients, category=category,
                            user=user)
            recipe.save()
            return render(request, 'recipe/index.html', {'form': form})
    else:
        form = RecipeForm()





