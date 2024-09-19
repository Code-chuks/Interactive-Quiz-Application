# quiz/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet
from . import views

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)  # API route for quizzes

urlpatterns = [
    # Web views
    path('register/', views.register, name='register'),
    path('home/', views.quiz_home, name='quiz-home'),

    # API routes
    path('api/', include(router.urls)),

    # Login and logout views
    path('accounts/', include('django.contrib.auth.urls')),
]
