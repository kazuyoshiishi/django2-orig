from django.contrib import admin

# Register your models here.
from django.contrib import admin
from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail', 'created_at', 'memo', 'DONE') 
    list_display_links = ('name', 'detail','memo', 'DONE') 
admin.site.register(Todo, TodoAdmin)