from django.db import models
from students.models import Student

class HostelRoom(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    current_occupants = models.IntegerField()

class HostelAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(HostelRoom, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField(null=True, blank=True)
