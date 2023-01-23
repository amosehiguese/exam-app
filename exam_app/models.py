from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    questions = models.ManyToManyField('Question', related_name='exams')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_exams')
    duration = models.DurationField()
    pass_score = models.IntegerField()
    active = models.BooleanField(default=True)
    max_attempt = models.IntegerField(default=1)
