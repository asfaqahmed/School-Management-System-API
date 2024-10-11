from rest_framework import viewsets
from .models import Room, HostelAssignment
from .serializers import RoomSerializer, HostelAssignmentSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class HostelAssignmentViewSet(viewsets.ModelViewSet):
    queryset = HostelAssignment.objects.all()
    serializer_class = HostelAssignmentSerializer
