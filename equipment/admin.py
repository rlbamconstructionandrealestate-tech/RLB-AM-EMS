from django.contrib import admin

from .models import Equipment



@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):


    list_display = (

        "asset_number",
        "name",
        "category",
        "status",
        "current_location",
        "purchase_price",
        "current_value",
        "created_at",

    )


    list_filter = (

        "status",
        "category",
        "manufacturer",

    )


    search_fields = (

        "asset_number",
        "name",
        "manufacturer",
        "model",

    )


    readonly_fields = (

        "created_at",
        "updated_at",

    )


    ordering = (

        "-created_at",

    )


    fieldsets = (

        (
            "Equipment Information",
            {

                "fields": (

                    "asset_number",
                    "name",
                    "category",
                    "manufacturer",
                    "model",
                    "status",

                )

            }
        ),


        (
            "Location & Value",
            {

                "fields": (

                    "current_location",
                    "purchase_price",
                    "current_value",
                    "purchase_date",

                )

            }
        ),


        (
            "Media & Description",
            {

                "fields": (

                    "image",
                    "description",

                )

            }
        ),


        (
            "System Information",
            {

                "fields": (

                    "created_at",
                    "updated_at",

                )

            }
        ),

    )