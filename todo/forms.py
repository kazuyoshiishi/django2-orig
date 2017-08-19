from django.forms import ModelForm
from todo.models import Todo

class TodoForm(ModelForm):
    """TODO_Form"""
    class Meta:
        model = Todo
        fields = ('name', 'detail', 'memo', 'dones')