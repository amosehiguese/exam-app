import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    questions = models.ManyToManyField('Question', related_name='exams')
    examiner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_exams')
    duration = models.DurationField()
    pass_score = models.IntegerField()
    active = models.BooleanField(default=True)
    max_attempt = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        db_table = 'exams'


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    choices = models.ManyToManyField('Choice', related_name='questions')
    image = models.ImageField(upload_to='question_image')
    correct_choice = models.ForeignKey('Choice', on_delete=models.SET_NULL, related_name='correct_for', null=True)

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        db_table = 'questions'
    

class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text

    class Meta:
        db_table = 'choices'

class ExamParticipation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    answers = models.ManyToManyField(Choice, through='Answer')

class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    participation = models.ForeignKey(ExamParticipation, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField()
    
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    name = models.CharField(max_length=255)
    description = models.TextField()
    exams = models.ManyToManyField('Exam', related_name='courses')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_courses')

    def __str__(self) -> str:
        return  self.name

class StudentGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User, related_name='group')
    exams = models.ManyToManyField('Exam', related_name='groups')

    def __str__(self) -> str:
        return self.name

class ExamConfiguration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    exam = models.OneToOneField('Exam', on_delete=models.CASCADE, related_name='configuration')
    number_of_questions = models.IntegerField()
    duration = models.DurationField()
    attempts_allowed = models.IntegerField()
    randomize_questions = models.BooleanField(default=True)
    randomize_answers = models.BooleanField(default=True)
    show_result = models.BooleanField(default=True)
    show_answers = models.BooleanField(default=False)
    show_score = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Configuration for {self.exam.name}'

class ExamResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField()
    passed = models.BooleanField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'score:{self.score}, passed:{self.passed}'