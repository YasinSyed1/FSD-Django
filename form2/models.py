from django.db import models

# Create your models here.

class Person1(models.Model):
    name = models.CharField(max_length=255)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()

    