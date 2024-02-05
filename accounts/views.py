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

# View for user registration or updating details separately
class UserDetailsRegistrationView(generics.CreateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Retrieve the authenticated user
        user = self.request.user
        # Check if user details already exist, update them if they do
        userdetails_instance, created = UserDetails.objects.get_or_create(user=user)
        serializer.save(user=user, full_name=userdetails_instance.full_name, address=userdetails_instance.address, photo=userdetails_instance.photo)

    def get(self, request, *args, **kwargs):
        # Retrieve user details if they exist
        userdetails_instance = UserDetails.objects.filter(user=self.request.user).first()
        if userdetails_instance:
            serializer = UserDetailsSerializer(userdetails_instance)
            return Response(serializer.data)
        else:
            # Return a 404 response if user details are not found
            return Response({"detail": "User details not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        # Retrieve user details and update them
        userdetails_instance = UserDetails.objects.filter(user=self.request.user).first()
        serializer = UserDetailsSerializer(userdetails_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# View for retrieving and updating user details
class UserDetailsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retrieve user details for the authenticated user
        return self.request.user.userdetails

    def put(self, request, *args, **kwargs):
        # Retrieve and update user details
        userdetails_instance = self.get_object()
        serializer = self.serializer_class(userdetails_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# View for user registration
class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

# View for user login
class CustomUserLoginView(LoginView):
    serializer_class = CustomUserSerializer

# View for user logout
class CustomUserLogoutView(LogoutView):
    permission_classes = [permissions.IsAuthenticated]

# View for changing user password
class CustomUserPasswordChangeView(PasswordChangeView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

# View for resetting user password
class CustomUserPasswordResetConfirmView(PasswordResetConfirmView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

# View for Google social login
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    serializer_class = CustomUserSerializer

# View for Facebook social login
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    serializer_class = CustomUserSerializer

# View for GitHub social login
class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    serializer_class = CustomUserSerializer
