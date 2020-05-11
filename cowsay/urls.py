from django.urls import path
from cowsay import views

url_paths = [
    path('', views.index, name='homepage')
]
