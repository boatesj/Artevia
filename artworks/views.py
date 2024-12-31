from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Artwork
from .forms import ArtworkForm, CategoryForm

def index(request):
    """Home page of the Artevia project"""
    return render(request, 'artworks/index.html')


# List views
def category_list(request):
    """Display a list of all categories"""
    categories = Category.objects.all()
    return render(request, 'artworks/category_list.html', {'categories': categories})

def artwork_list(request):
    """Display a list of all artworks"""
    artworks = Artwork.objects.all()
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks})

# Detail view
def artwork_detail(request, pk):
    """Display details of a single artwork"""
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})

# Add views
def add_artwork(request):
    """Add a new artwork"""
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artwork_list')
    else:
        form = ArtworkForm()
    return render(request, 'artworks/add_artwork.html', {'form': form})

def add_category(request):
    """Add a new category"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'artworks/add_category.html', {'form': form})

# Edit views
def edit_artwork(request, pk):
    """Edit an existing artwork"""
    artwork = get_object_or_404(Artwork, pk=pk)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artwork_list')
    else:
        form = ArtworkForm(instance=artwork)
    return render(request, 'artworks/edit_artwork.html', {'form': form})

def edit_category(request, pk):
    """Edit an existing category"""
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'artworks/edit_category.html', {'form': form})
