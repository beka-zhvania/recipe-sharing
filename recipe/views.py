from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewRecipeForm
from django.contrib.auth.decorators import login_required
from .models import Recipe

def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = NewRecipeForm(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user # the author should be whoever adds the form
            recipe.save()
            return redirect('recipe:recipes')
    else:
        form = NewRecipeForm()

    return render(request, 'create_recipe.html', {'form': form})

def recipe_details(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_details.html', {'recipe':recipe})