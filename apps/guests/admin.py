from django.contrib import admin
from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organization",
        "email",
        "contacted",
        "created_at",
    )

    list_filter = (
        "contacted",
        "created_at",
    )

    search_fields = (
        "name",
        "organization",
        "email",
    )

    readonly_fields = ("created_at",)
