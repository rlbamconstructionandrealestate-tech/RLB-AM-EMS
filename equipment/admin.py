from django.contrib import admin
from django.utils.html import format_html

from .models import Equipment, EquipmentCategory


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "name",
    )


@admin.action(description="Mark selected equipment as Available")
def mark_available(modeladmin, request, queryset):
    queryset.update(status="Available")


@admin.action(description="Mark selected equipment as Working")
def mark_working(modeladmin, request, queryset):
    queryset.update(status="Working")


@admin.action(description="Mark selected equipment as Maintenance")
def mark_maintenance(modeladmin, request, queryset):
    queryset.update(status="Maintenance")


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "asset_number",
        "name",
        "category",
        "manufacturer",
        "model",
        "status",
        "current_location",
        "daily_rate",
        "is_active",
    )

    list_display_links = (
        "asset_number",
        "name",
    )

    search_fields = (
        "asset_number",
        "name",
        "registration_number",
        "serial_number",
        "engine_number",
        "chassis_number",
        "manufacturer",
        "model",
    )

    list_filter = (
        "status",
        "category",
        "manufacturer",
        "is_active",
        "purchase_date",
        "created_at",
    )

    ordering = (
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "image_preview_large",
    )

    actions = [
        mark_available,
        mark_working,
        mark_maintenance,
    ]

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "category",
                    "asset_number",
                    "status",
                    "is_active",
                ),
            },
        ),

        (
            "Equipment Details",
            {
                "fields": (
                    "manufacturer",
                    "model",
                    "manufacture_year",
                    "registration_number",
                    "serial_number",
                    "engine_number",
                    "chassis_number",
                ),
            },
        ),

        (
            "Purchase Information",
            {
                "fields": (
                    "purchase_date",
                    "purchase_price",
                ),
            },
        ),

        (
            "Rental Charges",
            {
                "fields": (
                    "daily_rate",
                    "weekly_rate",
                    "monthly_rate",
                ),
            },
        ),

        (
            "Location",
            {
                "fields": (
                    "current_location",
                ),
            },
        ),

        (
            "Photo",
            {
                "fields": (
                    "image",
                    "image_preview_large",
                ),
            },
        ),

        (
            "Description",
            {
                "fields": (
                    "description",
                ),
            },
        ),

        (
            "System Information",
            {
                "classes": (
                    "collapse",
                ),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="45" style="border-radius:5px; object-fit:cover;">',
                obj.image.url,
            )
        return "-"

    image_preview.short_description = "Photo"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="300" style="border-radius:10px;">',
                obj.image.url,
            )
        return "No Image"

    image_preview_large.short_description = "Image Preview"