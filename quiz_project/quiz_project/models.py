from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    question = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    choice4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

class UserQuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
