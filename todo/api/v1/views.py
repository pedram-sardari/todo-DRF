from rest_framework import viewsets
from .serializer import TaskSerializer
from todo.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
