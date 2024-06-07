from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from item.models import *

from .forms import *


@login_required
def add_items(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = AddItems(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.seller = request.user
            form.save()
            messages.success(request, "Item Added Successfully!")
            return redirect('dashboard:index')
        else:
            # Print form errors to debug issues
            print(form.errors)
            messages.error(request, "There was an issue with the form.")
            return redirect('item:add-items')

    else:
        form = AddItems()

    context = {
        'form': form,
        'categories': categories,
    }

    return render(request, 'frontpages/add-items.html', context)


def edit_items(request, item_id):
    categories = Category.objects.all()
    item = get_object_or_404(Product, pk=item_id)

    if request.method == 'POST':
        form = AddItems(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form = form.save(commit=False)
            form.seller = request.user
            form.save()
            messages.success(request, "Item Updated Successfully!")
            return redirect('dashboard:index')
        else:
            # Print form errors to debug issues
            print(form.errors)
            messages.error(request, "There was an issue with the form.")
            return redirect('item:edit-items')

    else:
        form = AddItems(instance=item)

    context = {
        'form': form,
        'item': item,
        'categories': categories,
    }

    return render(request, 'frontpages/edit_items.html', context)


@login_required
def delete_items(request, pk):
    item = get_object_or_404(Product, pk=pk, seller=request.user)
    item.delete()

    return redirect('dashboard:index')
