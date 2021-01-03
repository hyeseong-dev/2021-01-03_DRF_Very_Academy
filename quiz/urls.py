from django.urls import path, include
from quiz.views  import Quiz, RandomQuestion, QuizQuestion

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions'),
]
