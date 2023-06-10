from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_description': forms.Textarea(attrs={'class': 'form-control'}),
        }