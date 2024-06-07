from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
    "email",
    "username",
    "first_name",
    "is_admin",
    "is_customer",
    "is_seller",
    ]

admin.site.register(CustomUser, CustomUserAdmin)