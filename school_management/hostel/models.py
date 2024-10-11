from django.db import models
from students.models import Student

class Room(models.Model):
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Room {self.number}"

class HostelAssignment(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    assigned_date = models.DateField()

    def __str__(self):
        return f"{self.student} assigned to Room {self.room.number}"
