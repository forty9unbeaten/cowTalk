from django.urls import path
from cowsay import views

url_paths = [
    path('', views.index, name='homepage'),
    path('/history', views.history_view, name='history')
]
