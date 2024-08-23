from django.db import models
from django.contrib.auth.models import User


# from

class Task(models.Model):
    class Priority(models.IntegerChoices):
        HIGH = 1, 'High'
        MEDIUM = 2, 'Medium'
        LOW = 3, 'Low'

    class Status(models.IntegerChoices):
        DONE = 1, 'Done'
        IN_PROGRESS = 2, 'In Progress'
        UN_DONE = 3, 'Un-Done'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    status = models.IntegerField(choices=Status.choices, default=Status.UN_DONE)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
