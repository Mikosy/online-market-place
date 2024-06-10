from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from item.models import *
from conversation.models import Conversation


@login_required
def index(request):
    items = Product.objects.filter(seller=request.user)
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    query = request.GET.get('q')
    if query:
        object_list = items.filter(name__icontains=query)
    else:
        object_list = items

    args = {
        'items': items,
        'conversations': conversations,
        'object_list':object_list
    }

    return render(request, 'dashboard/index.html', args)


