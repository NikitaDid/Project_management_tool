from django.shortcuts import render
from .models import Project

def projects_list(request):
    projects = Project.objects.all() #Get all projects from db
    return render(request, 'projects/projects_list.html',{'projects': projects})

