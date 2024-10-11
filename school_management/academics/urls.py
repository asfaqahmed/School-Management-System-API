from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Import views from academics app

router = DefaultRouter()
router.register(r'subjects', views.SubjectViewSet)  # Register views

urlpatterns = [
    path('', include(router.urls)),
]
