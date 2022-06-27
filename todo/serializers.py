from rest_framework import serializers
from .models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    # согл. документации
    class Meta:
        model = Todo
        fields = ('id', 'title')

class TodoDetailSerializer(serializers.ModelSerializer):
    # согл. документации
    class Meta:
        model = Todo
        fields = '__all__'
