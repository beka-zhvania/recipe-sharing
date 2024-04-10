from django.contrib import admin
from .models import Recipe, Category, Favorite


# Register models to be visible in the admin UI.
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Favorite)
