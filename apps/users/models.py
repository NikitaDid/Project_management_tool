from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin','Admin'),
        ('manager','Manager'),
        ('developer','Developer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='developer')
    team = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
