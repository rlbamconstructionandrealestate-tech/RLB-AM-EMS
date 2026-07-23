from django.contrib import admin
from .models import MaintenanceRecord



@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):


    list_display = (

        "equipment",

        "title",

        "service_date",

        "status",

        "technician",

        "cost",

    )


    list_display_links = (

        "equipment",

        "title",

    )



    list_filter = (

        "status",

        "service_date",

    )



    search_fields = (

        "equipment__name",

        "equipment__asset_number",

        "title",

        "technician",

    )



    ordering = (

        "-service_date",

    )



    list_per_page = 25




    fieldsets = (


        (
            "Maintenance Details",
            {

                "fields": (

                    "equipment",

                    "title",

                    "description",

                    "status",

                )

            }

        ),




        (
            "Service Information",
            {

                "fields": (

                    "service_date",

                    "next_service_date",

                    "technician",

                    "cost",

                )

            }

        ),


    )




    actions = [

        "mark_completed",

        "mark_pending",

    ]




    def mark_completed(self, request, queryset):

        queryset.update(
            status="completed"
        )


        self.message_user(
            request,
            "Selected maintenance records marked as completed."
        )



    mark_completed.short_description = (
        "Mark selected maintenance as completed"
    )





    def mark_pending(self, request, queryset):

        queryset.update(
            status="pending"
        )


        self.message_user(
            request,
            "Selected maintenance records marked as pending."
        )



    mark_pending.short_description = (
        "Mark selected maintenance as pending"
    )