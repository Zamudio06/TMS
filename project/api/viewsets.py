from rest_framework import status, viewsets

from api.serializers import TaskSerializer
from task_management.models import Task
from rest_framework.permissions import AllowAny


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
