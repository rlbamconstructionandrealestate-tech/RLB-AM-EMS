from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Enterprise User Administration
    Only system administrators should create users.
    Supported operational roles:
        • Managing Director
        • Director
        • Manager
        • Secretary
    """

    list_display = (
        "username",
        "first_name",
        "last_name",
        "role",
        "department",
        "is_staff",
        "is_superuser",
        "is_active",
        "is_active_employee",
    )

    list_display_links = (
        "username",
        "first_name",
        "last_name",
    )

    list_filter = (
        "role",
        "department",
        "is_staff",
        "is_superuser",
        "is_active",
        "is_active_employee",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "employee_id",
        "phone",
    )

    ordering = (
        "role",
        "first_name",
        "last_name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "last_login",
        "date_joined",
    )

    fieldsets = (

        (
            "Account Information",
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),

        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "profile_picture",
                )
            },
        ),

        (
            "Employment",
            {
                "fields": (
                    "employee_id",
                    "role",
                    "department",
                    "job_title",
                    "is_active_employee",
                )
            },
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

        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "Create New Employee Account",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "employee_id",
                    "role",
                    "department",
                    "job_title",
                    "phone",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ),
            },
        ),
    )