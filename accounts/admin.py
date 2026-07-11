from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "first_name",
        "last_name",
        "role",
        "department",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "role",
        "department",
        "is_active",
        "is_staff",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "RLB-AM Information",
            {
                "fields": (
                    "employee_id",
                    "role",
                    "department",
                    "job_title",
                    "phone",
                    "profile_picture",
                    "is_active_employee",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )