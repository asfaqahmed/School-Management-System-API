from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # Remove or rename 'admission_date'
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_boarder',)  # Remove or rename 'admission_date'
