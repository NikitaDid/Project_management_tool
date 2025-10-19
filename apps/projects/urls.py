from django.urls import path
from .views import projects_list

app_name = 'projects' #Nmaespacing for templates
urlpatterns = [
    path('', projects_list, name='projects_list')
]