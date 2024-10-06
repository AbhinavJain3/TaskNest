from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        new_todo = Todo(user=request.user, todo_name=task, due_date=due_date, priority=priority)
        new_todo.save()
        messages.success(request, 'Task added successfully!')
        return redirect('home-page')

    all_todos = Todo.objects.filter(user=request.user).order_by('-priority', 'due_date')
    overdue_todos = all_todos.filter(due_date__lt=timezone.now().date(), status=False)
    context = {
        'todos': all_todos,
        'overdue_todos': overdue_todos,
    }
    return render(request, 'todoapp/todo.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')
    return render(request, 'todoapp/register.html', {})

def LogoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home-page')
        else:
            # messages.error(request, 'Invalid username or password.')
            return redirect('home-page')
    
    return render(request, 'todoapp/login.html', {})

@login_required
def DeleteTask(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('home-page')

@login_required
def UpdateTask(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        todo.todo_name = request.POST.get('task')
        todo.due_date = request.POST.get('due_date')
        todo.priority = request.POST.get('priority')
        todo.status = request.POST.get('status') == 'on'
        todo.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('home-page')
    context = {'todo': todo}
    return render(request, 'todoapp/update_task.html', context)