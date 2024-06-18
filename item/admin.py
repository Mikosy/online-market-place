from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'seller','category',
                    'available', 'created_at']
    list_filter = ['available', 'created_at']
    list_editable = ['price', 'available']


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Transaction)
