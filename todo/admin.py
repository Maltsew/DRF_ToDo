from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    # поля модели, которые видны в списке
    list_display = ('id', 'title', 'description', 'date', 'done')
    list_display_links = ('id', 'title')
    # по каким полям модели возможен поиск
    search_fields = ('id', 'title', 'description')
    # модификация в списке атрибутов
    list_editable = ('done',)
    list_filter = ('done',)


admin.site.register(Todo, TodoAdmin)

