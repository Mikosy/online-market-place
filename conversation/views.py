from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
# models
from item.models import Product
from .models import *

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Product, pk=item_pk)

    # check if the creator of the item wants to access this page
    if item.seller == request.user.is_seller:
        return redirect('index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # Ensure item has 'created_by' attribute
            if not hasattr(item, 'seller'):
                form.add_error(None, 'The item does not have a "created_by" attribute.')
            else:
                conversation = Conversation.objects.create(item=item)
                conversation.members.add(request.user)
                conversation.members.add(item.seller)
                conversation.save()

                conversation_message = form.save(commit=False)
                conversation_message.conversation = conversation
                conversation_message.created_by = request.user
                conversation_message.save()

            return redirect('item-detail', item.id)
    else:
        form = ConversationMessageForm()

    args = {
        'form': form,
    }

    return render(request, 'conversation/new.html', args)

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    data = {
        'conversations': conversations
    }

    return render(request, 'conversation/inbox.html', data)

def converstaion_details(request, pk):
    detail = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        conversation_message = form.save(commit=False)
        conversation_message.conversation = detail
        conversation_message.created_by = request.user
        conversation_message.save()

        detail.save()

        return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {'detail':detail, 'form':form })


# def navbar(request):
#     if request.user.is_authenticated:
#         # Get the number of unique conversations the user is a part of
#         conversations = Conversation.objects.filter(members=request.user).distinct()
#         no_of_inboxes = conversations.count()
#     else:
#         no_of_inboxes = 0
#     print("no of inbox is =========>", no_of_inboxes)
#
#     return render(request, 'include/navbar.html', {'no_of_inboxes': no_of_inboxes})
