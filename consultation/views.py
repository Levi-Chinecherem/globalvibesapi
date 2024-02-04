# consultation/views.py
from rest_framework import generics
from rest_framework import permissions
from .models import Consultation, ConsultationNotification
from .serializers import ConsultationSerializer, ConsultationNotificationSerializer
from rest_framework.response import Response

class ConsultationListView(generics.ListCreateAPIView):
    """
    API view to list and create consultation messages.
    """
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
        
class ConsultationDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a specific consultation message.
    """
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConsultationNotificationView(generics.ListAPIView):
    """
    API view to list consultation notifications for a user.
    """
    queryset = ConsultationNotification.objects.all()
    serializer_class = ConsultationNotificationSerializer  # Create this serializer if not already done
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ConsultationNotification.objects.filter(user=self.request.user)
