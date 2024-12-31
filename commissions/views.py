from django.shortcuts import render, get_object_or_404, redirect
from .models import Commission
from .forms import CommissionForm
from django.contrib import messages

# Create your views here.

# List View
def commission_list(request):
    """Display a list of all commissions"""
    commissions = Commission.objects.all()
    return render(request, 'commissions/commission_list.html', {'commissions': commissions})

# Detail View
def commission_detail(request, pk):
    """Display details of a single commission"""
    commission = get_object_or_404(Commission, pk=pk)
    return render(request, 'commissions/commission_detail.html', {'commission': commission})

# Add View
def add_commission(request):
    """Add a new commission"""
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Commission added successfully!")
            return redirect('commission_list')
        else:
            messages.error(request, "Failed to add commission. Please correct the errors below.")
    else:
        form = CommissionForm()
    return render(request, 'commissions/add_commission.html', {'form': form})

# Edit View
def edit_commission(request, pk):
    """Edit an existing commission"""
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission)
        if form.is_valid():
            form.save()
            messages.success(request, "Commission updated successfully!")
            return redirect('commission_list')
        else:
            messages.error(request, "Failed to update commission. Please correct the errors below.")
    else:
        form = CommissionForm(instance=commission)
    return render(request, 'commissions/edit_commission.html', {'form': form})

# Delete View
def delete_commission(request, pk):
    """Delete an existing commission"""
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        commission.delete()
        messages.success(request, "Commission deleted successfully!")
        return redirect('commission_list')
    return render(request, 'commissions/delete_commission.html', {'commission': commission})

