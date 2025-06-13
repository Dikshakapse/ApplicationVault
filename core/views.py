from rest_framework import viewsets,permissions
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.telegram import send_telegram_message
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer  
    permission_classes = [permissions.IsAuthenticated] 
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        send_telegram_message(f"📌 New Job Added:\n{instance.position} at {instance.company_name}")
        


@api_view(['GET'])
@permission_classes([AllowAny])
def public_info(request):
    return Response({"message": "This is a public endpoint. No authentication needed!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_dashboard(request):
    user = request.user
    return Response({
        "message": f"Hello {user.username}, this is your private dashboard.",
        "email": user.email
    })
@api_view(['GET'])
def test_telegram_bot(request):
    send_telegram_message("👋 Hello! This is a test message from your Django bot 💬")
    return Response({"message": "Telegram test message sent!"})