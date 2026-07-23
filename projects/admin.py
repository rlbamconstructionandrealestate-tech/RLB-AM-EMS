from django.contrib import admin

from .models import (
    Project,
    ProjectMilestone,
    ProjectExpense,
    ProjectActivity,
)



# =====================================================
# PROJECT ADMIN
# =====================================================


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):


    list_display = (

        "project_code",

        "name",

        "client",

        "status",

        "priority",

        "progress",

        "contract_value",

        "created_at",

    )



    list_filter = (

        "status",

        "priority",

        "created_at",

    )



    search_fields = (

        "project_code",

        "name",

        "client__company_name",

        "location",

    )



    readonly_fields = (

        "created_at",

        "updated_at",

    )



    ordering = (

        "-created_at",

    )





# =====================================================
# PROJECT MILESTONE ADMIN
# =====================================================


@admin.register(ProjectMilestone)
class ProjectMilestoneAdmin(admin.ModelAdmin):


    list_display = (

        "name",

        "project",

        "status",

        "due_date",

    )



    list_filter = (

        "status",

        "due_date",

    )



    search_fields = (

        "name",

        "project__name",

    )





# =====================================================
# PROJECT EXPENSE ADMIN
# =====================================================


@admin.register(ProjectExpense)
class ProjectExpenseAdmin(admin.ModelAdmin):


    list_display = (

        "project",

        "category",

        "amount",

        "date",

        "created_by",

    )



    list_filter = (

        "category",

        "date",

    )



    search_fields = (

        "project__name",

        "description",

    )





# =====================================================
# PROJECT ACTIVITY ADMIN
# =====================================================


@admin.register(ProjectActivity)
class ProjectActivityAdmin(admin.ModelAdmin):


    list_display = (

        "project",

        "user",

        "created_at",

    )



    search_fields = (

        "project__name",

        "message",

    )