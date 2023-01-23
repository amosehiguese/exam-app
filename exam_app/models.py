from django.db import models

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=255)
    