from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreationForm
from django.contrib.auth import login


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # log in immediately after registration
            return redirect('profile')
    else:
        form = CreationForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')