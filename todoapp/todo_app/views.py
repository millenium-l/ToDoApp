from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskCreateForm

# Create your views here.
# takes a request and returns a response
#map the view on a url file
# not necesarry
def hello(request):
    return HttpResponse("<h1>This is our basic todo app<h1>")

# returning html requests
def index(request):
    context = {
        'name': 'lee'
    }
    return render(request, 'todo_app/index.html', context)

# taking request from models for users to viewers to use it
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_app/list.html', {'tasks':tasks})

def task_detail(request, id):
    tasks = get_object_or_404(Task, id=id) # we are passing an argument
    return render(request, 'todo_app/detail.html', {'task':tasks})


from django.shortcuts import render, redirect
from .forms import TaskCreateForm

def task_create(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')  # Make sure 'list' is a valid URL name
    else:
        form = TaskCreateForm()  # Create a new form instance for GET requests
    
    # Render the form with errors (if any) or as a new form
    return render(request, 'todo_app/create.html', {'form': form})

def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TaskCreateForm(instance=task)


    return render(request, 'todo_app/update.html', {'form':form})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    
    return render(request, 'todo_app/delete.html', {'task':task})