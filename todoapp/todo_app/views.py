from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required 
from django.views.generic import View, DetailView, ListView

# logindecorator is used to allow specific users to access specific documents

# Create your views here.
# takes a request and returns a response
#map the view on a url file
# not necesarry
def hello(request):
    return HttpResponse("<h1>This is our basic todo app</h1>")

# returning html requests
def index(request):
    context = {
        'name': 'lee'
    }
    return render(request, 'todo_app/index.html', context)

# taking request from models for users to viewers to use it

# enables better handling of http requSests
class TaskListView(View):
    template_name = 'todo_app/list.html'

    def get(self, request):
        tasks = Task.objects.all()
        paginator = Paginator(tasks, 2, orphans=1, allow_empty_first_page=True)# orphans are used to increase the numbers of tasks in the last page
        page = request.GET.get('page')

        try:
            paginated_tasks = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page.
            paginated_tasks = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page of results.
            paginated_tasks = paginated_tasks.page(paginator.num_pages)

            context = {'tasks':paginated_tasks, 'title':'list tasks'}

        return render(request, self.template_name, context)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo_app/detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task'
        return context

"""def task_detail(request, id):
    tasks = get_object_or_404(Task, id=id) # we are passing an argument
    return render(request, 'todo_app/detail.html', {'task':tasks})
"""

from django.shortcuts import render, redirect
from .forms import TaskCreateForm

@login_required
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

@login_required
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

@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    
    return render(request, 'todo_app/delete.html', {'task':task})


