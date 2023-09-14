from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('new/', views.create_recipe, name='new'),
    path('<int:pk>/', views.recipe_details, name='recipe_details'),
    path('<int:pk>/edit', views.edit_recipe, name='edit')
]
