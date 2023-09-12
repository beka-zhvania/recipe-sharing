from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('new/', views.create_recipe, name='new')
]
