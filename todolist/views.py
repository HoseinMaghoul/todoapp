import re
from django.contrib.auth.forms import UserChangeForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from todolist.forms import UserCreationForm
from .models import TodoList
from .forms import UserCreationForm, UserChangeForm
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    todos = TodoList.objects.all()
    return render(request, 'todolist/home.html', {'todos':todos})

    



def add_todo(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist:home')
        

    else:
        form = UserCreationForm()

    return render(request, 'todolist/add_todo.html', {'form':form})


def todo(request, t_id):
    todo = get_object_or_404(TodoList, pk=t_id)
    return render(request, 'todolist/todo.html', {'todo':todo})
    




def edit(request, t_id):
    todo = get_object_or_404(TodoList, pk=t_id)
    if request.method == 'POST':

        form = UserChangeForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todolist:home')
    
    else:
        form = UserChangeForm(instance=todo)

    return render(request, 'todolist/edit.html', {'form':form, 'todo':todo})



