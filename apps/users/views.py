from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_view(request):
    return HttpResponse("Users app is working!")