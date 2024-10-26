from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.

def show(request):
    tasks = Task.objects.all()  
    return render(request, "all.html", context={"tasks": tasks})

 
def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all")
    else:
        form = PostForm()
    return render(request, "add.html", {'form': form})
        

 
def update(request, pk):
    Post = Task.objects.filter(id=pk).first()
    if Post:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=Post)
            if form.is_valid():
                form.save()
                return redirect("all")
        else:
            form = PostForm(instance=Post)
        return render(request, "update.html", {'form': form})
    else:
        return HttpResponse("Not founded")

def delete(request, pk):
    Post = Task.objects.filter(id=pk).first()
    if Post:
        if request.method == 'POST':
            Post.delete()
            return redirect("all")
        else:
            return render(request, "delete.html", {'post': Post})
        



def get(request, pk):
    tasks = Task.objects.filter(id = pk).first()
    if tasks:
        return render(request, "get.html", context={"tasks": tasks})
    else:
        return HttpResponse("No such task")
