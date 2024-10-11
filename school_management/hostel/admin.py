from django.contrib import admin
from .models import Room, HostelAssignment

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')
    search_fields = ('number',)

@admin.register(HostelAssignment)
class HostelAssignmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'room', 'assigned_date')
    list_filter = ('assigned_date',)
    search_fields = ('student__first_name', 'student__last_name', 'room__number')
