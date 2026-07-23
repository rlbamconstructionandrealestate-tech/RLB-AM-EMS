from django.urls import path

from . import views


app_name = "employees"


urlpatterns = [

    # ==========================================
    # EMPLOYEE DASHBOARD
    # ==========================================
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),


    # ==========================================
    # EMPLOYEE LIST
    # ==========================================
    path(
        "list/",
        views.employee_list,
        name="list"
    ),


    # ==========================================
    # CREATE EMPLOYEE
    # ==========================================
    path(
        "create/",
        views.employee_create,
        name="create"
    ),


    # ==========================================
    # UPDATE EMPLOYEE
    # ==========================================
    path(
        "update/<int:pk>/",
        views.employee_update,
        name="update"
    ),


    # ==========================================
    # DELETE EMPLOYEE
    # ==========================================
    path(
        "delete/<int:pk>/",
        views.employee_delete,
        name="delete"
    ),


    # ==========================================
    # ATTENDANCE
    # ==========================================
    path(
        "attendance/",
        views.attendance,
        name="attendance"
    ),


    # ==========================================
    # PAYROLL
    # ==========================================
    path(
        "payroll/",
        views.payroll,
        name="payroll"
    ),

]