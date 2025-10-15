from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email', 'role','team')