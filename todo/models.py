from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254) 
    password = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.username}"
    

class Task(models.Model):
    name = models.CharField(max_length=50)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    user= models.ForeignKey(User,  on_delete=models.CASCADE)
    is_active = models.BooleanField()
    def __str__(self):
        return f"{self.task_name}"
    
