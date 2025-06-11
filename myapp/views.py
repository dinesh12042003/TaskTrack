from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ToDoForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def insert(request):
    form = ToDoForm()
    if request.method=='POST':
        data = ToDoForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('ToDo')
    return render(request, 'edit.html', {'form' : form})

def edit(request, id):
    currTask=ToDoList.objects.get(id=id)
    data = ToDoForm(instance=currTask)
    if request.method=='POST':
        data = ToDoForm(request.POST, instance=currTask)
        if data.is_valid():
            data.save()
        return redirect('ToDo')
    return render(request, 'edit.html', {'form': data})

def delete(request, id):
    Student=ToDoList.objects.get(id=id)
    Student.delete()
    return redirect('ToDo')

def ToDo(request):
    Data=ToDoList.objects.all()
    return render(request, 'ToDo.html', {'Data':Data})