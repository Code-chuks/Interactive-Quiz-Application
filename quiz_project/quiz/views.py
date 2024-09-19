# quiz/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .forms import CustomUserCreationForm
from .models import Quiz
from .serializers import QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz-home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def quiz_home(request):
    return render(request, 'quiz/home.html')
