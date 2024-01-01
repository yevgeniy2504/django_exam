from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .forms import RecipeForm
from .models import Recipe


# Create your views here.

links = [
    '<a href="/recipe/recipes/">recipes</a>',
    '<a href="/recipe/recipes/new/">new recipe</a>',
    '<a href="/recipe/login/">login</a>',
    '<a href="/recipe/logout/">logout</a>',
    '<a href="/recipe/signup/">signup</a>',
    '<a href="/recipe/password_reset/">password reset</a>',
    '<a href="/recipe/password_reset_done/">password reset done</a>',
    '<a href="/recipe/password_reset_confirm/">password reset confirm</a>',
    '<a href="/recipe/password_reset_complete/">password reset complete</a>',
    '<a href="/recipe/password_change/">password change</a>',
    '<a href="/recipe/password_change_done/">password change done</a>',
    '<a href="/recipe/user/">user</a>',
    '<a href="/recipe/user_edit/">user edit</a>',
    '<a href="/recipe/user_delete/">user delete</a>',
    '<a href="/recipe/user_detail/">user detail</a>',
]


def index(request):
    return HttpResponse("Hello, world. You're at the recipe index.", links)


def recipes(request):
    recipes = Recipe.objects.order_by('-pub_date')
    context = {'recipes': recipes}
    return render(request, 'recipe/recipes.html', context, links)


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe/recipe.html', {'recipe': recipe}, links)

@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.pub_date = timezone.now()
            recipe.save()
            return redirect('recipe:recipe', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipe/new_recipe.html', {'form': form}, links)


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.pub_date = timezone.now()
            recipe.save()
            return redirect('recipe:recipe', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/edit_recipe.html', {'form': form}, links)


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('recipe:recipes')


@login_required
def add_ingredient(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.ingredient_set.create(name=request.POST['name'], quantity=request.POST['quantity'], unit=request.POST['unit'])
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def delete_ingredient(request, recipe_id, ingredient_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredient = get_object_or_404(recipe.ingredient_set, pk=ingredient_id)
    ingredient.delete()
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def add_instruction(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.instruction_set.create(text=request.POST['text'])
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def delete_instruction(request, recipe_id, instruction_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    instruction = get_object_or_404(recipe.instruction_set, pk=instruction_id)
    instruction.delete()
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def add_image(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.image_set.create(image=request.FILES['image'])
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def delete_image(request, recipe_id, image_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    image = get_object_or_404(recipe.image_set, pk=image_id)
    image.delete()
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def add_tag(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.tag_set.create(name=request.POST['name'])
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def delete_tag(request, recipe_id, tag_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    tag = get_object_or_404(recipe.tag_set, pk=tag_id)
    tag.delete()
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def add_category(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.category_set.create(name=request.POST['name'])
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def delete_category(request, recipe_id, category_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    category = get_object_or_404(recipe.category_set, pk=category_id)
    category.delete()
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def add_cooking_time(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.cookingtime_set.create(name=request.POST['name'])
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def delete_cooking_time(request, recipe_id, cooking_time_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    cooking_time = get_object_or_404(recipe.cookingtime_set, pk=cooking_time_id)
    cooking_time.delete()
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def add_author(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.author_set.create(name=request.POST['name'])
    return redirect('recipe:recipe', recipe_id=recipe.id)


@login_required
def delete_author(request, recipe_id, author_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    author = get_object_or_404(recipe.author_set, pk=author_id)
    author.delete()
    return redirect('recipe:recipe', recipe_id=recipe.id)


def login(request):
    return render(request, 'recipe/login.html', links)


def logout(request):
    return render(request, 'recipe/logout.html', links)


def signup(request):
    return render(request, 'recipe/signup.html', links)


def password_reset(request):
    return render(request, 'recipe/password_reset.html', links)


def password_reset_done(request):
    return render(request, 'recipe/password_reset_done.html', links)


def password_reset_confirm(request):
    return render(request, 'recipe/password_reset_confirm.html', links)


def password_reset_complete(request):
    return render(request, 'recipe/password_reset_complete.html', links)


def password_change(request):
    return render(request, 'recipe/password_change.html', links)


def password_change_done(request):
    return render(request, 'recipe/password_change_done.html', links)


def user(request):
    return render(request, 'recipe/user.html', links)


def user_edit(request):
    return render(request, 'recipe/user_edit.html', links)


def user_delete(request):
    return render(request, 'recipe/user_delete.html', links)


def user_detail(request):
    return render(request, 'recipe/user_detail.html', links)


