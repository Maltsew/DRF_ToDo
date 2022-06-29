from django.shortcuts import render
from rest_framework import generics
from todo.serializers import TodoDetailSerializer, TodoListSerializer
from todo.models import Todo
from todo.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class TodoCreateView(generics.CreateAPIView):
    """ создание записей """
    serializer_class = TodoDetailSerializer


class TodoListView(generics.ListAPIView):
    """только отображение выюбранных записей"""
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated, )


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """обновление, получение, удаление данных об одном объекте"""
    serializer_class = TodoDetailSerializer
    queryset = Todo.objects.all()
    # авторизация с помощью токенов. к api запрещен доступ через web и авторизация через cookie
    # можно указать в кортеже и другие методы, но в таком случае в каждую вью необходимо добавить этот метод
    # authentication_classes = (TokenAuthentication, ) -> перенесено в settings
    # доступ - редактировать запись может тот, кто ее создал
    permission_classes = (IsOwnerOrReadOnly, )
