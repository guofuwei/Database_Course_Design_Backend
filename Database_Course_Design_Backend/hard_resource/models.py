from django.db import models


class HardResource(models.Model):
    id = models.AutoField(primary_key=True)
    resource_name = models.CharField(max_length=100)
    resource_num = models.IntegerField()
