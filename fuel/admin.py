from django.contrib import admin

from .models import FuelRecord


@admin.register(FuelRecord)
class FuelRecordAdmin(admin.ModelAdmin):

    list_display = (
        "date",
        "machine",
        "fuel_station",
        "litres",
        "price_per_litre",
        "total_cost",
    )

    search_fields = (
        "machine__name",
        "operator",
        "fuel_station",
        "receipt_number",
    )

    list_filter = (
        "fuel_type",
        "payment_method",
        "date",
    )

    ordering = (
        "-date",
    )