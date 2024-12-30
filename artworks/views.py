from django.shortcuts import render, get_object_or_404
from .models import Category, Artwork

# Create your views here.

def category_list(request):
    """Display a list of all categories"""
    categories = Category.objects.all()
    return render(request, 'artworks/category_list.html', {'categories': categories})

def artwork_list(request):
    """Display a list of all artworks"""
    artworks = Artwork.objects.all()
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks})

def artwork_detail(request, pk):
    """Display details of a single artwork"""
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})
