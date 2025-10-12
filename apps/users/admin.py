from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username','email','role','team','is_staff']
    fieldsets = UserAdmin.fieldsets + (  #fieldsets controls the form when editing/creating a user in the admin.
        (None, {'fields': ('role','team')}),  #('Section Title', {'fields': (list_of_fields)})
    )


