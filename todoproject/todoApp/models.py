from datetime import date
from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=12)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

class Task(models.Model):
    taskname=models.CharField(max_length=500)
    completed=models.CharField(max_length=100)
    date=models.CharField(max_length=100)

    def __str__(self):
        return self.taskname
