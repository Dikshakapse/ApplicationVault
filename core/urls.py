# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobApplicationViewSet
from .views import test_telegram_bot,test_telegram_bot, public_info, user_dashboard
router = DefaultRouter()
router.register(r'applications', JobApplicationViewSet, basename='applications')

urlpatterns = router.urls
from django.urls import path
from . import views

urlpatterns = [
    path('public-info/', public_info, name='public-info'),
    path('user-dashboard/', user_dashboard, name='user-dashboard'),
    path('test-telegram/', test_telegram_bot),
    path('', include(router.urls)),
]