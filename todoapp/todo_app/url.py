# mapping our views from the views file
from operator import index # not a must
from django.urls import path
# importing the view you want to map fro the url
from .views import hello, index, task_list, task_detail, task_create

urlpatterns = [
    path('', task_list, name='list'),
    path('detail/<int:id>/', task_detail, name='detail'),# we are passing an argument
    path('create/', task_create, name='create'),
    path('hello/', hello),
    path('index/', index, name='index'),
]