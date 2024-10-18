from django.urls import path

from .views import add_task_view, view_tasks


urlpatterns = [
    path('add-task/', add_task_view, name='add-task-view'),
    path('view-tasks/', view_tasks, name='view-tasks-view'),
]
