from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewRecipeForm, EditRecipeForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Recipe, Category, Favorite

def recipes(request):
    recipes = Recipe.objects.all()
    category_id = request.GET.get('category', 0)  # use 0 as a default category
    categories = Category.objects.all()
    

    query = request.GET.get('query', '')

    if category_id:
        # if category is specified, only use recipes from that category
        recipes = recipes.filter(category_id=category_id)

    if query:
        # if searched string is contained in name, description or ingredient list, then it should be returned
        recipes = recipes.filter(Q(name__icontains=query) | Q(short_description__icontains=query) | Q(ingredients__icontains=query))
        

    return render(request, 'recipes.html', {
        'recipes': recipes,
        'categories': categories,
        'category_id': int(category_id)
    })


def carousel(request):
    recipes = Recipe.objects.all()

    return render(request, 'carousel.html', {
        'recipes': recipes,
    })


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
    is_favorite = Favorite.objects.filter(user=request.user, recipe=recipe).exists()
    return render(request, 'recipe_details.html', {'recipe':recipe, 'is_favorite' : is_favorite})


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
    
@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    recipe.delete()

    return redirect('recipe:recipes')


@login_required
def favorites(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    favorite_recipes = [favorite.recipe for favorite in favorites]
    return render(request, 'favorites.html', {
        'favorite_recipes' : favorite_recipes
    })

@login_required
def add_to_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    return redirect('recipe:recipe_details', pk=recipe.id)


@login_required
def remove_from_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    Favorite.objects.filter(user=request.user, recipe=recipe).delete()
    return redirect('recipe:recipe_details', pk=recipe.id)