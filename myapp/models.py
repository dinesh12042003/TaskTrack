from django.db import models

# Create your models here.
class ToDoList(models.Model):
    task=models.CharField(max_length=100)
    task_desc=models.CharField(max_length=300)
    priority=models.CharField(max_length=30)
    assigned_on=models.DateField()
    deadline=models.DateField()
    status=models.CharField(max_length=30)