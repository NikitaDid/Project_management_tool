from django.urls import path
from .views import tasks_list

app_name = 'tasks'
urlpatterns = [
    path('', tasks_list, name='tasks_list'),
]