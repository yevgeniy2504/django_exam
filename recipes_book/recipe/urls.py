from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/', views.recipes, name='recipes'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),
    path('recipe/new/', views.new_recipe, name='new_recipe'),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipe/<int:recipe_id>/add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('recipe/<int:recipe_id>/delete_ingredient/<int:ingredient_id>/', views.delete_ingredient, name='delete_ingredient'),
    path('recipe/<int:recipe_id>/add_instruction/', views.add_instruction, name='add_instruction'),
    path('recipe/<int:recipe_id>/delete_instruction/<int:instruction_id>/', views.delete_instruction, name='delete_instruction'),
    path('recipe/<int:recipe_id>/add_image/', views.add_image, name='add_image'),
    path('recipe/<int:recipe_id>/delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('recipe/<int:recipe_id>/add_tag/', views.add_tag, name='add_tag'),
    path('recipe/<int:recipe_id>/delete_tag/<int:tag_id>/', views.delete_tag, name='delete_tag'),
    path('recipe/<int:recipe_id>/add_category/', views.add_category, name='add_category'),
    path('recipe/<int:recipe_id>/delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('recipe/<int:recipe_id>/add_cooking_time/', views.add_cooking_time, name='add_cooking_time'),
    path('recipe/<int:recipe_id>/delete_cooking_time/<int:cooking_time_id>/', views.delete_cooking_time, name='delete_cooking_time'),
    path('recipe/<int:recipe_id>/add_author/', views.add_author, name='add_author'),
    path('recipe/<int:recipe_id>/delete_author/<int:author_id>/', views.delete_author, name='delete_author'),
]

