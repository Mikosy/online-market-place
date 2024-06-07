from django.db import models

from item.models import Product
from core.models import CustomUser


class Conversation(models.Model):
    item = models.ForeignKey(Product, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

    def __int__(self):
        return self.item


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name='created_messages', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
