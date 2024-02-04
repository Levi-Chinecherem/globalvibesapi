# moderators/views.py
from rest_framework import generics, permissions
from .models import Moderator, ModeratorNotification
from .serializers import ModeratorSerializer, ModeratorNotificationSerializer
from rest_framework.response import Response
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404

class ModeratorListView(generics.ListAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.IsAdminUser]

class PromoteToModeratorView(generics.CreateAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(CustomUser, pk=user_id)
        serializer.save(user=user)

        # Notify the user about being promoted to moderator
        notification = ModeratorNotification.objects.create(
            user=user,
            message="You have been promoted to moderator. Enjoy your new privileges!"
        )

        return Response({"message": "User promoted to moderator successfully."})
