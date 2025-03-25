from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'is_staff', 'is_superuser')
    search_fields = ('name', 'email', 'mobile')
    ordering = ('id',)

    # Define fields for editing user details
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'mobile')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields required when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'mobile', 'password1', 'password2'),
        }),
    )
