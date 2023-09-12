from django import forms
from .models import Recipe

form_styling = 'w-full py-14 px-6 rounded-xl text-black'

class NewRecipeForm(forms.ModelForm):


    class Meta:
        model = Recipe
        fields = ['name', 'category', 'image', 'short_description', 'ingredients', 'steps']

    
    def __init__(self, *args, **kwargs):
        input_style = 'w-full rounded-md focus:ring focus:ri focus:ri border-gray-700 text-gray-900'
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': input_style})
        self.fields['category'].widget.attrs.update({'class': input_style})
        self.fields['short_description'].widget.attrs.update({
            'class': input_style,
            'placeholder': ' A breakfast sandwich...'
        })
        self.fields['ingredients'].widget.attrs.update({
            'class': input_style,
            'placeholder': ' 2 Onions, 100g milk...',
            'rows': 2
        })
        self.fields['steps'].widget.attrs.update({
            'class': input_style,
            'placeholder': ' 1. Cut onions\n 2. Add salt\n ... ',
            'id': 'stepsField'
        })
        self.fields['steps'].initial = "1. " 

        self.fields['image'].widget.attrs.update({'class': 'w-full rounded-md focus:ring focus:ri focus:ri border-white-700 text-white-900'})

