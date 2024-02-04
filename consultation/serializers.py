# consultation/serializers.py
from rest_framework import serializers
from .models import Consultation, ConsultationNotification

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp', 'admin_only']

class ConsultationNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationNotification
        fields = '__all__'
