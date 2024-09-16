from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('quiz-home')  # Redirect to your home page or quiz page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Add this new home view
def quiz_home(request):
    return render(request, 'quiz/home.html')
