from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='tasks')
urlpatterns = router.urls
