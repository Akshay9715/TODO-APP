from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

def Home(request):
    todos = Todo.objects.order_by('-id')
    return render(request,'todo/index.html',{'todos' : todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        Todo.objects.create(title=title,desc=desc)
    
    return redirect('Home')

def complete_todo(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.completed = True
    todo.save()

    return redirect('Home')

def delete_todo(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    
    return redirect('Home')