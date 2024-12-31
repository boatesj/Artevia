from django.shortcuts import render, get_object_or_404, redirect
from .models import Commission
from .forms import CommissionForm
from django.contrib import messages

# List all commissions
def commission_list(request):
    commissions = Commission.objects.all()
    return render(request, 'commissions/commission_list.html', {'commissions': commissions})

# Detail view for a specific commission
def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    return render(request, 'commissions/commission_detail.html', {'commission': commission})

# Add a new commission
def add_commission(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Commission added successfully!")
            return redirect('commission_list')
        else:
            messages.error(request, "Error adding commission. Please check the form.")
    else:
        form = CommissionForm()
    return render(request, 'commissions/add_commission.html', {'form': form})

# Edit an existing commission
def edit_commission(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission)
        if form.is_valid():
            form.save()
            messages.success(request, "Commission updated successfully!")
            return redirect('commission_detail', pk=commission.pk)
        else:
            messages.error(request, "Error updating commission. Please check the form.")
    else:
        form = CommissionForm(instance=commission)
    return render(request, 'commissions/edit_commission.html', {'form': form})

# Delete a commission
def delete_commission(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        commission.delete()
        messages.success(request, "Commission deleted successfully!")
        return redirect('commission_list')
    return render(request, 'commissions/delete_commission.html', {'commission': commission})
