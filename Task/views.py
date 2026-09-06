from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from .forms import TaskForm
from .models import Task

def home(request):
    submitted = request.GET.get("submitted") == "true"
    return render(request, "home.html", {"submitted": submitted})

def add_task(request):
    #formset = formset_factory(TaskForm,max_num=1,validate_max=True)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('intro')}?submitted=true")
    else:
        form = TaskForm()
    return render(request, "add-task.html", {"form": form})
def view_tasks(request):
    tasks=Task.objects.all()
    return render(request,"display-tasks.html",{"tasks":tasks})
def update_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('view_tasks')}")
    else:
        return render(request, "display-tasks.html", {})