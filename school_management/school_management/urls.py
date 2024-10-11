from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', include('students.urls')),
    path('api/academics/', include('academics.urls')),
    path('api/hostel/', include('hostel.urls')),
    path('api/fees/', include('fees.urls')),
    path('api/notifications/', include('notifications.urls')),
]
