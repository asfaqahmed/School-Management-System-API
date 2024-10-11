from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('student', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('student__first_name', 'student__last_name', 'message')
