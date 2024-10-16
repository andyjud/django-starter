from django.shortcuts import render, redirect
from .tasks import count_task

def home_view(request):
    return render(request, 'home.html')

def count_view(request):
    count_task.delay()
    return redirect('home')