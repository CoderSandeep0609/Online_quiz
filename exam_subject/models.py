from django.db import models
from django.contrib.auth.models import User

class AttemptAnswer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE )
    question = models.CharField(max_length=1000)
    selected_answer = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
    chk_id=models.IntegerField()

class Feedback(models.Model):
    user=models.CharField()
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=100)
    message=models.TextField()
