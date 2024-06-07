from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# paginating items
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from item.models import *

from item.forms import *


@login_required
def index(request):
    items = Product.objects.filter(available=True)
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all().order_by('name')[:10]

    if category_id:
        items = Product.objects.filter(category_id=category_id)

    # creating pagination object for categories
    p = Paginator(items, 12)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    query = request.GET.get('q')
    if query:
        object_list = items.filter(name__icontains=query)
    else:
        object_list = items

    for item in items:
        # item.available = item.quantity > 0
        if item.expiration_date and item.quantity < 0:
            item.available = False

    args = {
        'items': items,
        'categories': categories,
        'page_obj': page_obj,
        'query': query,
        'object_list': object_list,
        'category_id': int(category_id)
    }

    return render(request, 'frontpages/index.html', args)


@login_required
def item_detail(request, item_pk):
    detail = get_object_or_404(Product, pk=item_pk, available=True)
    related_items = Product.objects.filter(category=detail.category, available=True).exclude(pk=item_pk)[0:3]
    args = {
        'detail': detail,
        'related_items': related_items,
    }

    return render(request, 'frontpages/item-detail.html', args)


