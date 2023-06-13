from django.db import models
from student.models import Student
from hard_resource.models import HardResource


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    max_select_num = models.IntegerField()
    selected_num = models.IntegerField(default=0)


class SC(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class RC(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resource = models.ForeignKey(HardResource, on_delete=models.CASCADE)
