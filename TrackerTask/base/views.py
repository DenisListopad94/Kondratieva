from django.shortcuts import render
from .models import Task


#Списоки словарей
tasks = [
    {"task": "Завершить проект", "status": "started", "category": "work"},
    {"task": "Купить продукты", "status": "pending", "category": "personal"},
    {"task": "Подготовка к экзаменам", "status": "started", "category": "study"},
    {"task": "Уборка в квартире", "status": "completed", "category": "personal"},
    {"task": "Отправить отчет", "status": "pending", "category": "work"},
]

users = [
    {"name": "Иван", "age": 22, "phone": "123-456-7890", "photo": "base/images/photo1.jpg"},
    {"name": "Анна", "age": 30, "phone": "098-765-4321", "photo": "base/images/photo2.jpg"},
    {"name": "Петр", "age": 25, "phone": "555-555-5555", "photo": "base/images/photo3.jpg"},
    {"name": "Мария", "age": 28, "phone": "444-444-4444", "photo": "base/images/photo4.jpg"},
]


def home(request):
    return render(request, 'base/home.html', {'title': 'Главная страница'})


def tasks_view(request):
    return render(request, 'base/tasks.html', {'title': 'Список задач', 'tasks': tasks})


def users_view(request):
    return render(request, 'base/users.html', {'title': 'Список пользователей', 'users': users})


def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'base/all_tasks.html', {'tasks': tasks})


def high_priority_tasks(request):
    tasks = Task.objects.filter(priority="h")
    return render(request, 'base/high_priority_tasks.html', {'tasks': tasks})


def medium_priority_tasks(request):
    tasks = Task.objects.filter(priority="m").exclude(status="None")
    return render(request, 'base/high_priority_tasks.html', {'tasks': tasks})


def tasks_starting_with_create(request):
    tasks = Task.objects.filter(title__startswith="Создать")
    return render(request, 'base/create_tasks.html', {'tasks': tasks})