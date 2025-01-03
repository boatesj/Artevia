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
@login_required
@user_passes_test(is_admin)
def category_list(request):
    """Display categories and handle add/edit functionality."""
    categories = Category.objects.all()
    form = CategoryForm()
    edit_form = None
    category_to_edit = None

    if 'edit_id' in request.GET:
        category_to_edit = get_object_or_404(Category, id=request.GET['edit_id'])
        edit_form = CategoryForm(instance=category_to_edit)

    if request.method == 'POST':
        if 'category_id' in request.POST:
            # Editing an existing category
            category = get_object_or_404(Category, id=request.POST['category_id'])
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                messages.success(request, "Category updated successfully!")
            else:
                messages.error(request, "Failed to update category.")
        else:
            # Adding a new category
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Category added successfully!")
            else:
                messages.error(request, "Failed to add category.")
        return redirect('category_list')

    context = {
        'categories': categories,
        'form': form,
        'edit_form': edit_form,
        'category_to_edit': category_to_edit,
    }
    return render(request, 'artworks/categories.html', context)




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
    """Add a new category using categories.html"""
    categories = Category.objects.all()  # Fetch all categories for display

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect('category_list')  # Redirect to the list of categories
        else:
            messages.error(request, "Failed to add category. Please correct the errors below.")
    else:
        form = CategoryForm()  # Provide an empty form for GET requests

    return render(request, 'artworks/categories.html', {
        'form': form,
        'categories': categories,
        'editing': False,  # Not editing, this is for adding a category
    })


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
    """Edit an existing category using categories.html"""
    category = get_object_or_404(Category, pk=pk)
    categories = Category.objects.all()  # Fetch all categories for display

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect('category_list')  # Redirect to the list of categories
        else:
            messages.error(request, "Failed to update category. Please correct the errors below.")
    else:
        form = CategoryForm(instance=category)  # Prepopulate form with category data

    return render(request, 'artworks/categories.html', {
        'form': form,
        'categories': categories,
        'editing': True,  # Flag to indicate we're editing
        'category_to_edit': category,  # Pass the category being edited
    })


@login_required
@user_passes_test(is_admin)
def category_detail(request, category_id):
    """View to edit a specific category"""
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect('category_list')  # Redirect back to the list
        else:
            messages.error(request, "Failed to update category. Please correct the errors below.")
    else:
        form = CategoryForm(instance=category)
    return render(request, 'artworks/category_details.html', {'form': form, 'category': category})



def artwork_list(request):
    """Display a list of all artworks"""
    query = request.GET.get('q', '')
    artworks = Artwork.objects.filter(title__icontains=query) if query else Artwork.objects.all()
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks, 'query': query})


@login_required
@user_passes_test(is_admin)
def delete_category(request, category_id):
    """Delete a category"""
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, "Category deleted successfully!")
    return redirect('category_list')



