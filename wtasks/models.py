from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Assigned_Task = models.CharField(max_length=200)
    Task_Status = models.IntegerField()
    Salary = models.IntegerField()

    def str(self):
        return self.Name


