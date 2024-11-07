from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)
    mobile_num = models.CharField(max_length=20)
    hobbies = models.CharField(max_length=200, default='Cricket, Kabaddi')
    