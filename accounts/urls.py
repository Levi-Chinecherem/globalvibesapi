from django.urls import path
from django.contrib import admin
from .views import UserDetailsRegistrationView, CustomUserRegistrationView, CustomUserLoginView, CustomUserLogoutView, \
    CustomUserPasswordChangeView, CustomUserPasswordResetConfirmView, GoogleLogin, FacebookLogin, GitHubLogin, UserDetailsView

urlpatterns = [
    path('secret/place/of/admin/', admin.site.urls),
    path('register/', CustomUserRegistrationView.as_view(), name='register'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),
    path('password/change/', CustomUserPasswordChangeView.as_view(), name='password_change'),
    path('password/reset/confirm/', CustomUserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('social/login/google/', GoogleLogin.as_view(), name='google_login'),
    path('social/login/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('social/login/github/', GitHubLogin.as_view(), name='github_login'),
    path('userdetails/register', UserDetailsRegistrationView.as_view(), name='userdetails-registration'),
    path('userdetails/', UserDetailsView.as_view(), name='user_details'),
]
