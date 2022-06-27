# базовый permissions
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """stackoverflow - drf owner permission"""
    def has_object_permission(self, request, view, obj):
        # использование безоп. методов
        if request.method in permissions.SAFE_METHODS:
            return True
        # пользователь обекта - request user. с помощью куки в сессии - авторизован ли
        return obj.user == request.user