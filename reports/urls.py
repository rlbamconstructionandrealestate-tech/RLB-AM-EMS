from django.urls import path

from . import views


app_name = "reports"



urlpatterns = [

    # =====================================================
    # REPORT DASHBOARD
    # =====================================================

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),



    # =====================================================
    # ANALYTICS
    # =====================================================

    path(
        "analytics/",
        views.analytics,
        name="analytics"
    ),



    # =====================================================
    # EQUIPMENT REPORTS
    # =====================================================

    path(
        "equipment/",
        views.equipment_reports,
        name="equipment_reports"
    ),



    # =====================================================
    # FINANCIAL REPORTS
    # =====================================================

    path(
        "financial/",
        views.financial_reports,
        name="financial_reports"
    ),



    # =====================================================
    # PROJECT REPORTS
    # =====================================================

    path(
        "projects/",
        views.project_reports,
        name="project_reports"
    ),



    # =====================================================
    # EXPORT
    # =====================================================

    path(
        "export/",
        views.export,
        name="export"
    ),

]