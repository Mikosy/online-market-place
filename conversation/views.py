from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
# models
from item.models import Product
from .models import *


def new_conversation(request, item_pk):
    item = get_object_or_404(Product, pk=item_pk)

    # check if the creator of the item wants to access this page
    if item.seller == request.user:
        return redirect('index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            converstation_message = form.save(commit=False)
            converstation_message.conversation = conversation
            converstation_message.created_by = request.user
            converstation_message.save()

            return redirect('item-detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    args = {
        'form': form,
    }

    return render(request, 'conversation/new.html', args)
