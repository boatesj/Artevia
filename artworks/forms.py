from django import forms
from .models import Artwork, Category

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'category', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the artwork...'}),
        }
        labels = {
            'title': 'Artwork Title',
            'description': 'Artwork Description',
            'category': 'Category',
            'image': 'Upload Image',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category name'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("A category with this name already exists.")
        return name

