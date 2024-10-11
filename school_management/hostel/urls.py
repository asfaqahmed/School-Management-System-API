from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, HostelAssignmentViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'assignments', HostelAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
