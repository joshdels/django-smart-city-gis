from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Organization, Office


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ["email"]
    list_display = ("email", "first_name", "last_name", "organization", "office", "role", "is_staff")
    search_fields = ("email", "first_name", "last_name", "organization")

    fieldsets = (
        (
            "User Info",
            {"fields": ("email", "first_name", "last_name", "role", "organization", "office")},
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
class OrganizationAdmin(admin.ModelAdmin):

    list_display = ("id", "name")
