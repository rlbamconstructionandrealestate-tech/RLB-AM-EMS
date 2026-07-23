from django.contrib import admin

from .models import Client, Contract

from projects.models import Project




# =====================================================
# PROJECT INLINE FOR CLIENT
# =====================================================


class ProjectInline(admin.TabularInline):

    model = Project

    extra = 0

    fields = (

        "project_code",

        "name",

        "status",

        "priority",

        "contract_value",

        "amount_paid",

    )

    readonly_fields = (

        "project_code",

        "name",

        "status",

        "priority",

        "contract_value",

        "amount_paid",

    )

    can_delete = False






# =====================================================
# CLIENT ADMIN
# =====================================================


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):


    inlines = [

        ProjectInline,

    ]



    list_display = (

        "company_name",

        "contact_person",

        "phone",

        "email",

        "industry",

        "status",

        "created_at",

    )



    search_fields = (

        "company_name",

        "contact_person",

        "email",

        "phone",

    )



    list_filter = (

        "status",

        "industry",

        "created_at",

    )



    ordering = (

        "company_name",

    )



    readonly_fields = (

        "created_at",

        "updated_at",

    )



    fieldsets = (

        (
            "Company Information",
            {

                "fields": (

                    "company_name",

                    "contact_person",

                    "industry",

                    "status",

                )

            }

        ),



        (
            "Contact Details",
            {

                "fields": (

                    "email",

                    "phone",

                    "address",

                )

            }

        ),



        (
            "Additional Information",
            {

                "fields": (

                    "notes",

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








# =====================================================
# CONTRACT ADMIN
# =====================================================


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):


    list_display = (

        "contract_number",

        "client",

        "project_name",

        "total_value",

        "start_date",

        "end_date",

        "status",

    )



    search_fields = (

        "contract_number",

        "project_name",

        "client__company_name",

    )



    list_filter = (

        "status",

        "start_date",

        "end_date",

    )



    ordering = (

        "-created_at",

    )



    readonly_fields = (

        "created_at",

        "updated_at",

    )



    autocomplete_fields = (

        "client",

    )



    fieldsets = (

        (
            "Contract Information",
            {

                "fields": (

                    "client",

                    "contract_number",

                    "project_name",

                    "status",

                )

            }

        ),



        (
            "Financial Details",
            {

                "fields": (

                    "total_value",

                )

            }

        ),



        (
            "Contract Duration",
            {

                "fields": (

                    "start_date",

                    "end_date",

                )

            }

        ),



        (
            "Description",
            {

                "fields": (

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