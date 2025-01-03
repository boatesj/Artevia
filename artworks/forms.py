from django import forms
from .models import Artwork, Category, Commission

# Artwork Form
class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'category', 'price', 'image', 'is_featured']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the artwork...'}),
            'price': forms.NumberInput(attrs={'min': 0, 'placeholder': 'Set a price in £'}),
        }
        labels = {
            'title': 'Artwork Title',
            'description': 'Artwork Description',
            'category': 'Category',
            'price': 'Price (£)',
            'image': 'Upload Image',
            'is_featured': 'Feature this Artwork',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title


# Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category name'}),
            'description': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Optional: Add a description'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("A category with this name already exists.")
        return name


# Commission Request Form
class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['description', 'price', 'due_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Provide details for the commission'}),
            'price': forms.NumberInput(attrs={'min': 0, 'placeholder': 'Proposed budget in £'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'description': 'Commission Details',
            'price': 'Budget (£)',
            'due_date': 'Due Date',
        }
