from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Todo

def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'app/index.html', { "todo_items": todo_items })

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date = current_date, text = content)
    print(created_obj)
    print(created_obj.id)
    length_of_todos = Todo.objects.all().count()
    print(length_of_todos)
    return redirect('/')

def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')