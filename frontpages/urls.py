from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('item-detail/<item_pk>/', item_detail, name='item-detail'),

]