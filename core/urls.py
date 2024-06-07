from django.urls import path

from core.views import *

app_name = "core"

urlpatterns = [
    path('admin-signup/', admin_signup , name="admin-signup"),
    path('customer-signup/', customer_signup , name="customer-signup"),
    path('seller-signup/', seller_signup , name="seller-signup"),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # for social login
    path('login/google/', google_login, name='google_login'),
    path('complete/google/', google_complete, name='google_complete'),
]

