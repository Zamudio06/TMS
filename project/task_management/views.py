from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_task_view(request):
    return render(request, 'task/add_task.html')

@login_required
def view_tasks(request):
    return render(request, 'task/view_tasks.html')
