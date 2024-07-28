# mapping our views from the views file
from operator import index
from django.urls import path
# importing the view you want to map fro the url
from .views import hello, index

urlpatterns = [
    path('', hello),
    path('index/', index, name='index')
]