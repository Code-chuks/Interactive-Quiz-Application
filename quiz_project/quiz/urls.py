from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration route
    path('home/', views.quiz_home, name='quiz-home'),    # Quiz home route
]
