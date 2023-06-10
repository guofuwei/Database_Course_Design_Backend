from django.db import models
from course.models import Course


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
