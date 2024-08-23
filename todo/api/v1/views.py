from django.utils import timezone
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serializer import TaskSerializer
from todo.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TodayTaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(deadline__day=timezone.now().day)


"""
add task , edit , change status, dele
task - week - day
don - unproress
"""
