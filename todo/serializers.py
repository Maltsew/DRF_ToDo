from rest_framework import serializers
from .models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    # согл. документации
    class Meta:
        model = Todo
        fields = ('id', 'title')

class TodoDetailSerializer(serializers.ModelSerializer):
    # пользователь из request при авторизации
    # убирает возможность менять пользователя

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # согл. документации
    class Meta:
        model = Todo
        fields = '__all__'
