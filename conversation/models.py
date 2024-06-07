from django.db import models

from item.models import Product


class Conversation(models.Model):
    item = models.ForeignKey(Product, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField('core.CustomUser', related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

    def __str__(self):
        return f"{self.item}-{self.memebers}"


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('core.CustomUser', related_name='created_messages', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.conversation}-{self.content}"
