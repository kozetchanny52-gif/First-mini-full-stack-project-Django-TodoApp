from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import RegistrationForm, TaskForm
from .models import Task, User as TaskUser

def get_task_user(request):
    task_user, _ = TaskUser.objects.get_or_create(username=request.user.username)
    return task_user

@login_required(login_url="login")
def home(request):
    submitted = request.GET.get("submitted") == "true"
    return render(request, "home.html", {"submitted": submitted})

@login_required(login_url="login")
def add_task(request):
    #formset = formset_factory(TaskForm,max_num=1,validate_max=True)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = get_task_user(request)
            task.save()
            return redirect(f"{reverse('intro')}?submitted=true")
    else:
        form = TaskForm()
    return render(request, "add-task.html", {"form": form})
@login_required(login_url="login")
def view_tasks(request):
    tasks=Task.objects.filter(user=get_task_user(request))
    return render(request,"display-tasks.html",{"tasks":tasks})

@login_required(login_url="login")
def update_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id, user=get_task_user(request))
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('view_tasks')}")
    return redirect("view_tasks")

@login_required(login_url="login")
@require_POST
def delete_task(request,task_id):
    task=get_object_or_404(Task,pk=task_id,user=get_task_user(request))
    task.delete()
    return redirect("view_tasks")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("intro")
    if request.method == "POST":
        username=request.POST.get("username", "")
        password=request.POST.get("password", "")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("intro")
        messages.error(request,"Username or password is incorrect.")
    return render(request,"login.html")

def register_view(request):
    if request.user.is_authenticated:
        return redirect("intro")
    form=RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request,"Account created. You can now log in.")
        return redirect("login")
    return render(request,"register.html",{"form":form})

@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")