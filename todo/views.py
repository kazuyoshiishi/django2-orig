from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from todo.models import Todo
from todo.forms import TodoForm

# Create your views here.
def todo_list(request):
    """todo_list"""
    todos = Todo.objects.all().order_by('id')
    return render(request,
                  'todo/todo_list.html',     # 
                  {'todos': todos})         # 

def todo_edit(request, todo_id=None):
    """todo_edit"""
    if todo_id:   
        todo = get_object_or_404(Todo, pk=todo_id)
    else:        
        todo = Todo()

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)  
        if form.is_valid():    
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list')
    else:    # GET
        form = TodoForm(instance=todo)  

    return render(request, 'todo/todo_edit.html', dict(form=form, todo_id=todo_id))
    
def todo_del(request, todo_id):
    """todo_del"""
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todo:todo_list')

def todo_list_no(request):
    """todo_list_no"""
    todos = Todo.objects.all().order_by('id')
    return render(request,
                  'todo/todo_list_no.html',     # 
                  {'todos': todos})         # 
