from django import forms
from django.forms import ModelForm
from .models import Task

class TaskCreate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]