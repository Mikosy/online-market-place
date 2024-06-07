from django.shortcuts import render, redirect
from item.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from core.models import *

from .forms import AdminSignUpForm, CustomerSignUpForm, SellerSignUpForm

# third party login
from social_django.views import auth, complete
from social_core.exceptions import AuthCanceled

from django_countries import countries


 

def admin_signup(request):

    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.save()
            return redirect('core:login')  # Redirect to login page after successful signup
    else:
        form = AdminSignUpForm()
    return render(request, 'core/signup.html')


def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Additional logic for setting user role as customer
            user.is_customer = True
            user.save()
            return redirect('core:login')  # Redirect to login page after successful signup
    else:
        form = CustomerSignUpForm()
    return render(request, 'core/customer-signup.html')


def seller_signup(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Additional logic for setting user role as seller
            user.is_seller = True
            user.save()
            return redirect('core:login')  # Redirect to login page after successful signup
    else:
        form = SellerSignUpForm()

    all_countries = sorted(countries, key=lambda x: x.name)

    args = {
        'all_countries' : all_countries
    }

    return render(request, 'core/seller-signup.html', args )


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:index')
            else:
                messages.info(request, 'username OR password is incorrect')
                return redirect('core:login')

    context = {}
    return render(request, 'core/login.html', context)






# Handling auth for google
def google_login(request):
    # Redirect users to Google's login page
    return auth(request, 'google-oauth2')

def google_complete(request):
    # Handle the authentication callback from Google
    try:
        response = complete(request, 'google-oauth2')
    except AuthCanceled:
        # Handle case where authentication is canceled
        return HttpResponseBadRequest("Authentication Canceled")
    return response


# Logout
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('core:login')
