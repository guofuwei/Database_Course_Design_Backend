from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    student_id = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
