from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('tasks/', views.tasks_view, name='tasks'),  # Страница задач
    path('users/', views.users_view, name='users'),  # Страница пользователей
    path('tasks/all/', views.all_tasks, name='all_tasks'),
    path('tasks/high_priority/', views.high_priority_tasks, name='high_priority_tasks'),
    path('tasks/medium_priority/', views.medium_priority_tasks, name='medium_priority_tasks'),
    path('tasks/create/', views.tasks_starting_with_create, name='tasks_starting_with_create'),
]