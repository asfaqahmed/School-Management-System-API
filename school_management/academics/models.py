from django.db import models
from students.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)

class ClassSchedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10)
