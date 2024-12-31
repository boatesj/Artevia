from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Artwork
from .forms import ArtworkForm, CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    """Check if user is an admin"""
    return user.is_staff

def index(request):
    """Home page of the Artevia project"""
    return render(request, 'artworks/index.html')


# List views
def category_list(request):
    """Display a list of all categories"""
    query = request.GET.get('q', '')
    categories = Category.objects.filter(name__icontains=query) if query else Category.objects.all()
    return render(request, 'artworks/category_list.html', {'categories': categories, 'query': query})

def artwork_list(request):
    """Display a list of all artworks"""
    query = request.GET.get('q', '')
    artworks = Artwork.objects.filter(title__icontains=query) if query else Artwork.objects.all()
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks, 'query': query})

# Detail view
def artwork_detail(request, pk):
    """Display details of a single artwork"""
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})

# Add views
@login_required
@user_passes_test(is_admin)
def add_artwork(request):
    """Add a new artwork"""
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Artwork added successfully!")
            return redirect('artwork_list')
        else:
            messages.error(request, "Failed to add artwork. Please correct the errors below.")
    else:
        form = ArtworkForm()
    return render(request, 'artworks/add_artwork.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def add_category(request):
    """Add a new category"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect('category_list')
        else:
            messages.error(request, "Failed to add category. Please correct the errors below.")
    else:
        form = CategoryForm()
    return render(request, 'artworks/add_category.html', {'form': form})

# Edit views
@login_required
@user_passes_test(is_admin)
def edit_artwork(request, pk):
    """Edit an existing artwork"""
    artwork = get_object_or_404(Artwork, pk=pk)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, "Artwork updated successfully!")
            return redirect('artwork_list')
        else:
            messages.error(request, "Failed to update artwork. Please correct the errors below.")
    else:
        form = ArtworkForm(instance=artwork)
    return render(request, 'artworks/edit_artwork.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_category(request, pk):
    """Edit an existing category"""
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect('category_list')
        else:
            messages.error(request, "Failed to update category. Please correct the errors below.")
    else:
        form = CategoryForm(instance=category)
    return render(request, 'artworks/edit_category.html', {'form': form})
