from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Todo(models.Model):
    """Модель приложения to-do."""
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
