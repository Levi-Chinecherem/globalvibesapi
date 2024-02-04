# consultation/urls.py
from django.urls import path
from .views import ConsultationListView, ConsultationDetailView, ConsultationNotificationView

urlpatterns = [
    path('consultations/', ConsultationListView.as_view(), name='consultation-list-create'),
    path('consultations/<int:pk>/', ConsultationDetailView.as_view(), name='consultation-detail'),
    path('consultation-notifications/', ConsultationNotificationView.as_view(), name='consultation-notifications'),
]
