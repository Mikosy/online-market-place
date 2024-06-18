from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from item.models import *

from .forms import *

#for item upload with file
from django.contrib import messages
import pandas as pd
from datetime import datetime

import os



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
@login_required
def upload_products(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            try:
                df = pd.read_excel(excel_file)

                # Handle NaT values and non-strings explicitly
                def handle_expiration_date(x):
                    if pd.isna(x):
                        return None  # Keep as None
                    elif isinstance(x, str):  # Check if it's a string (potential ISO format)
                        try:
                            return pd.to_datetime(x).tz_localize(utc)  # Attempt conversion
                        except (ValueError, AttributeError):  # Handle invalid string format
                            return None
                    else:
                        return x  # Keep other data types as-is

                df['expiration_date'] = df['expiration_date'].apply(handle_expiration_date)

                for index, row in df.iterrows():
                    seller = CustomUser.objects.get(id=row['seller_id'])
                    category = Category.objects.get(id=row['category_id'])

                    # Handle image upload
                    image_file = None
                    if 'image' in request.FILES:  # Check if image file is uploaded
                        image_file = request.FILES['image']

                    product = Product.objects.create(
                        seller=seller,
                        name=row['name'],
                        description=row['description'],
                        price=row['price'],
                        category=category,
                        quantity=row['quantity'],
                        available=bool(row['available']),
                        expiration_date=row['expiration_date'],
                        image=image_file  # Assign image if uploaded
                    )

                    # Handle image saving (optional)
                    if image_file:
                        # Generate unique filename (optional)
                        filename = f'{product.id}_{image_file.name}'
                        filepath = os.path.join(settings.MEDIA_ROOT, 'products', filename)

                        # Save image to specified location
                        with open(filepath, 'wb') as f:
                            for chunk in image_file.chunks():
                                f.write(chunk)

                messages.success(request, 'Products uploaded successfully.')
                return redirect('/')
            except Exception as e:
                messages.error(request, f'Error uploading products: {e}')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = ExcelUploadForm()

    return render(request, 'frontpages/upload_products.html', {'form': form})
