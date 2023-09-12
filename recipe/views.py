from django.shortcuts import render, redirect
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