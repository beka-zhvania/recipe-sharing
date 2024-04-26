from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('new/', views.create_recipe, name='new'),
    path('<int:pk>/', views.recipe_details, name='recipe_details'),
    path('<int:pk>/edit', views.edit_recipe, name='edit'),
    path('<int:pk>/delete', views.delete_recipe, name='delete'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_to_favorites/<int:recipe_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:recipe_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('carousel/', views.carousel, name='carousel')
]
