from rest_framework import serializers
from .models import Room, HostelAssignment

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class HostelAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelAssignment
        fields = '__all__'
