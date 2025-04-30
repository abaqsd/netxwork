from django.contrib import admin
from django.urls import path, include
from accounts.views import AccountHomeRedirectView, HomePageView
from django.shortcuts import redirect
from accounts.views import mentor_chat
from accounts import views



def home_redirect(request):
    return redirect('/accounts/signup/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/login/', include('allauth.urls')),
    path('accounts/', AccountHomeRedirectView.as_view(), name='account-home'),
    path('auth/registration/', include('accounts.urls')),
    path('api/mentor/', mentor_chat, name='mentor_chat'),
]
