from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    questions = models.ManyToManyField('Question', related_name='exams')
    examiner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_exams')
    duration = models.DurationField()
    pass_score = models.IntegerField()
    active = models.BooleanField(default=True)
    max_attempt = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'exams'


class Question(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    choices = models.ManyToManyField('Choice', related_name='questions')
    correct_choice = models.ForeignKey('Choice', on_delete=models.SET_NULL, related_name='correct_for', null=True)

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        db_table = 'questions'
    

class Choice(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text

    class Meta:
        db_table = 'choices'

class ExamParticipation(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_participations')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='participations')
    score = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    answers = models.ManyToManyField(Choice, related_name='exam_participations', through='Answer')

class Answer(models.Model):
    participation = models.ForeignKey(ExamParticipation, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField()
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    exams = models.ManyToManyField('Exam', related_name='courses')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_courses')