from django.contrib import admin
from .models import Employee



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        "employee_id",
        "first_name",
        "last_name",
        "position",
        "department",
        "status",
    )


    search_fields = (
        "employee_id",
        "first_name",
        "last_name",
        "phone",
    )


    list_filter = (
        "status",
        "department",
        "employee_type",
    )