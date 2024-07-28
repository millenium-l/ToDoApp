from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes a request and returns a response
#map the view on a url file
def hello(request):
    return HttpResponse("<h1>This is our basic todo app<h1>")

# returning html requests
def index(request):
    context = {
        'name': 'lee'
    }
    return render(request, 'todo_app/index.html', context)
