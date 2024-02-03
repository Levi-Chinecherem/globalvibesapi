from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.views.registration import SocialLoginView
from dj_rest_auth.views.login import LoginView
from dj_rest_auth.views.logout import LogoutView
from dj_rest_auth.views.password_change import PasswordChangeView
from dj_rest_auth.views.password_reset import PasswordResetConfirmView
from .serializers import CustomUserSerializer, UserDetailsSerializer
from .models import CustomUser, UserDetails


class UserDetailsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.userdetails

    def put(self, request, *args, **kwargs):
        userdetails_instance = self.get_object()
        serializer = self.serializer_class(userdetails_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class CustomUserLoginView(LoginView):
    serializer_class = CustomUserSerializer

class CustomUserLogoutView(LogoutView):
    permission_classes = [permissions.IsAuthenticated]

class CustomUserPasswordChangeView(PasswordChangeView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomUserPasswordResetConfirmView(PasswordResetConfirmView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    serializer_class = CustomUserSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    serializer_class = CustomUserSerializer

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    serializer_class = CustomUserSerializer
