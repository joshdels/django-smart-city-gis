from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Organization, Office


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (
            "User Info",
            {"fields": ("username", "email", "role", "organization", "office")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
    )


@admin.register(Organization)
class Organization(admin.ModelAdmin):

    list_display = ("id", "name")
