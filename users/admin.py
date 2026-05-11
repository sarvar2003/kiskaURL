from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    ordering = ['id']

    list_display = [
        'id',
        'email',
        'username',
        'is_staff',
        'is_active',
    ]

    search_fields = [
        'email',
        'username',
    ]

    readonly_fields = [
        'date_joined',
        'date_updated',
    ]

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'username',
                'password',
            )
        }),

        ('Permissions', {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),

        ('Important dates', {
            'fields': (
                'last_login',
                'date_joined',
                'date_updated',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )