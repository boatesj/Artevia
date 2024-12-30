from django import forms
from .models import Artwork, Category

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'category', 'image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
