from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('add_task/', views.add_task, name='addTask'),
]