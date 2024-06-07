from django.urls import path

from .views import *

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>/', new_conversation, name='new'),
]
