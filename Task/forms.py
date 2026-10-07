from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as AuthUser
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        exclude=["user"]
        widgets={

            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter task's title"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "type":forms.Select(attrs={"class":"form-control"}),
            "is_complete":forms.CheckboxInput(attrs={"id":"checkbox"}),
            "deadline":forms.DateTimeInput(
            attrs={"type": "datetime-local","class":"form-control"},
            format="%Y-%m-%dT%H:%M"
        ),

        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model=AuthUser
        fields=("username",)