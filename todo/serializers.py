from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    # согл. документации
    class Meta:
        model = Todo
        fields = '__all__'
