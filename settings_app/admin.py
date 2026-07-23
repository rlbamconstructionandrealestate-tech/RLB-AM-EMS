from django.contrib import admin

from .models import (
    CompanyProfile,
    SystemPreference,
    NotificationSetting,
)





# =====================================================
# COMPANY PROFILE ADMIN
# =====================================================

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):


    list_display = (

        "company_name",

        "short_name",

        "email",

        "phone",

        "city",

        "country",

        "updated_at",

    )



    search_fields = (

        "company_name",

        "short_name",

        "email",

        "phone",

    )



    readonly_fields = (

        "created_at",

        "updated_at",

    )






# =====================================================
# SYSTEM PREFERENCE ADMIN
# =====================================================

@admin.register(SystemPreference)
class SystemPreferenceAdmin(admin.ModelAdmin):


    list_display = (

        "system_name",

        "enable_notifications",

        "enable_email",

        "enable_dark_mode",

        "maintenance_mode",

        "updated_at",

    )



    list_filter = (

        "enable_notifications",

        "enable_email",

        "enable_dark_mode",

        "maintenance_mode",

    )



    readonly_fields = (

        "created_at",

        "updated_at",

    )







# =====================================================
# NOTIFICATION SETTINGS ADMIN
# =====================================================

@admin.register(NotificationSetting)
class NotificationSettingAdmin(admin.ModelAdmin):


    list_display = (

        "user",

        "email_notifications",

        "project_updates",

        "payment_alerts",

        "equipment_alerts",

        "maintenance_alerts",

    )



    search_fields = (

        "user__username",

        "user__email",

    )



    list_filter = (

        "email_notifications",

        "project_updates",

        "payment_alerts",

        "equipment_alerts",

        "maintenance_alerts",

    )