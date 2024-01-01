from django.urls import path
from . import views
from .views import recipe_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('recipe_detail/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    # Добавим URL для new_recipe
]
