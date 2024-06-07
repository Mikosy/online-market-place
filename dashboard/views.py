from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from item.models import *


@login_required
def index(request):
    items = Product.objects.filter(seller=request.user)

    args = {
        'items': items
    }

    return render(request, 'dashboard/index.html', args)


