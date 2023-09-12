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
    creation_date= models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    ingredients = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.category})"


