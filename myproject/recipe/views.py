from django.shortcuts import render, redirect
from .forms.category_add_form import CategoryForm
from .forms.new_user_profile_form import AuthorForm
from .forms.new_recipe_form import RecipeForm
from .forms.add_ingridient import IngredientForm
from .models import Recipe


# Create your views here.
def index(request):
    links = [
        {'url': '/', 'text': 'Главная'},
        {'url': '/create_recipe', 'text': 'Создать рецепт'},
        {'url': '/create_category', 'text': 'Создать категорию'},
        {'url': '/create_user', 'text': 'Создать пользователя'},
        {'url': '/add_ingredient', 'text': 'Добавить ингредиент'},
    ]

    recipes = Recipe.objects.all()

    return render(request, 'recipe/index.html', {'links': links, 'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe/recipe.html', {'recipe': recipe})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # или куда вам нужно
    else:
        form = CategoryForm()

    return render(request, 'recipe/create_category.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # или куда вам нужно
    else:
        form = AuthorForm()

    return render(request, 'recipe/create_user.html', {'form': form})


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # или куда вам нужно
    else:
        form = RecipeForm()

    return render(request, 'recipe/create_recipe.html', {'form': form})


def add_ingredient(request):
    if request.method == 'POST':
        # Обработка POST-запроса, создание формы и сохранение данных
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # или куда вам нужно
    else:
        # Обработка GET-запроса, создание пустой формы
        form = IngredientForm()

    return render(request, 'recipe/add_ingredient.html', {'form': form})