from django import forms 
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'due_date', 'description', 'user', 'is_active')