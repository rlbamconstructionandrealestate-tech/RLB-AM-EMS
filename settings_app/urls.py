from django.urls import path

from . import views



app_name = "settings_app"





urlpatterns = [

    # =====================================================
    # SETTINGS DASHBOARD
    # =====================================================

    path(

        "",

        views.dashboard,

        name="dashboard"

    ),



    # =====================================================
    # COMPANY PROFILE
    # =====================================================

    path(

        "company/",

        views.company_profile,

        name="company"

    ),





    # =====================================================
    # SYSTEM PREFERENCES
    # =====================================================

    path(

        "system/",

        views.system_preferences,

        name="system"

    ),



    # =====================================================
    # NOTIFICATION SETTINGS
    # =====================================================

    path(

        "notifications/",

        views.notification_settings,

        name="notifications"

    ),



]