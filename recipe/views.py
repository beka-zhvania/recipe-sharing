from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewRecipeForm, EditRecipeForm
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

    return render(request, 'recipe_form.html', {
        'form': form,
        'title': 'Create a New Recipe',
        'button_text': 'Create Recipe'
    })

def recipe_details(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_details.html', {'recipe':recipe})


@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)

    if request.method == 'POST':
        form = EditRecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()

            return redirect('recipe:recipe_details', pk=recipe.id)

    else:
        form = EditRecipeForm(instance=recipe)

    return render(request, 'recipe_form.html', {
        'form': form,
        'title': f"Edit {recipe.name} recipe",
        'button_text': 'Update Recipe'
    })
    

