from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParticipantsViewSet, ColDebViewSet
router = DefaultRouter()
router.register('participants', ParticipantsViewSet, basename='participants')
router.register('count', ColDebViewSet, basename='count')
urlpatterns = [
] + router.urls
