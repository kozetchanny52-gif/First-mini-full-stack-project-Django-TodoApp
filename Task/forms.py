from django import forms
from .models import *
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"
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