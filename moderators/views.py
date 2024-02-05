# moderators/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404
from .models import Moderator, ModeratorNotification
from .serializers import ModeratorSerializer, ModeratorNotificationSerializer

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

class DemoteFromModeratorView(generics.DestroyAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        user_id = self.kwargs['user_id']
        return get_object_or_404(Moderator, user__id=user_id)

    def perform_destroy(self, instance):
        # Notify the user about being demoted from moderator
        notification = ModeratorNotification.objects.create(
            user=instance.user,
            message="You have been demoted from moderator. Your privileges have been revoked."
        )

        instance.delete()
        return Response({"message": "User demoted from moderator successfully."})
