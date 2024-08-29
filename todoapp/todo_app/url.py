# mapping our views from the views file
from operator import index # not a must
from django.urls import path
# importing the view you want to map fro the url
from .views import hello, index, TaskListView, TaskDetailView, task_create, task_update, task_delete
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('detail/<int:pk>', TaskDetailView.as_view(), name='detail'),# we are passing an argument
    path('update/<int:id>/', task_update, name='update'),# we are passing an argument
    path('delete/<int:id>/', task_delete, name='delete'),
    path('create/', task_create, name='create'),
    path('hello/', hello),
    path('index/', index, name='index'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]