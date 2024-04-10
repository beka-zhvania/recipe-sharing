from django.db import models
from django.contrib.auth.models import User


# category of the recipe (e.g. dessert)
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    short_description = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='recipe_images/')
    ingredients = models.TextField(blank=True)
    steps = models.TextField(blank=True)

    def ingredient_list(self):
        if self.ingredients:
            ingredient_list = [ingredient.strip() for ingredient in self.ingredients.split(',')]
            return ingredient_list
        else:
            return []
    
    def step_list(self):
        if self.steps:
            step_list = [step.strip() for step in self.steps.split('\n')]
            return step_list
        else:
            return []
    
    def __str__(self):
        return f"{self.name} ({self.category})"


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='favorited_by', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
        'user', 'recipe')  # Prevents the same recipe from being added multiple times by the same user

    def __str__(self):
        return f"{self.user} favorites {self.recipe}"