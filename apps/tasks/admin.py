from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','status','assigned_to','project','created_at')
    list_filter = ('status','project')
    search_fields = ('title',)
