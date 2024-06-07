from django.urls import path
from . views import *

app_name = 'item'


urlpatterns = [
    # add item
    path('add-items/', add_items, name='add-items'),
    path('edit-items/<str:item_id>/', edit_items, name='edit-items'),
    path('delete-items/<str:pk>/', delete_items, name='delete-items'),
]
