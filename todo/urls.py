"""
# таким образом данные будут доступны для всех
from rest_framework import routers
from .api import TodoViewSet


router = routers.DefaultRouter()
router.register('api/todo', TodoViewSet, 'todo')


urlpatterns = router.urls
"""

from django.contrib import admin
from django.urls import path, include
from todo.views import *

app_name = "todo"
urlpatterns = [
    path('api/todo/', TodoCreateView.as_view()),
    path('api/all/', TodoListView.as_view()),
    path('api/detail/<int:pk>', TodoDetailView.as_view())
]

