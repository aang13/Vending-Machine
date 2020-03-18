from django.db import models

class Employee(models.Model):
    first_name=models.CharField(max_length=15)
    lastname=models.CharField(max_length=10)
    employeeid=models.IntegerField()

    def __str__(self):
        return self.first_name
# Create your models here.
