from rest_framework import viewsets,permissions
from .models import JobApplication
from .serializers import JobApplicationSerializer


class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_classes=JobApplicationSerializer
    permisiion_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
