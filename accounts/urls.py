from django.urls import path
from .views import UserProfileSetupView

urlpatterns = [
    path('profile-setup/', UserProfileSetupView.as_view(), name='profile-setup'),
]
