from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Employee(models.Model):
	Employee_Id=models.IntegerField(primary_key = True)
	Employee_Name=models.CharField(max_length=50)
	Department_Name=models.CharField(max_length=50)


