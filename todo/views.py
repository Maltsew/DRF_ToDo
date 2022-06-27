from django.shortcuts import render
from rest_framework import generics
from todo.serializers import TodoDetailSerializer, TodoListSerializer
from todo.models import Todo
from todo.permissions import IsOwnerOrReadOnly


# Create your views here.
class TodoCreateView(generics.CreateAPIView):
    """ создание записей """
    serializer_class = TodoDetailSerializer


class TodoListView(generics.ListAPIView):
    """только отображение выюбранных записей"""
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """обновление, получение, удаление данных об одном объекте"""
    serializer_class = TodoDetailSerializer
    queryset = Todo.objects.all()
    # доступ - редактировать запись может тот, кто ее создал
    permission_classes = (IsOwnerOrReadOnly,)
