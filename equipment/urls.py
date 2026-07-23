from django.urls import path

from . import views


app_name = "equipment"



urlpatterns = [

    # ==========================
    # DASHBOARD
    # ==========================

    path(
        "dashboard/",
        views.equipment_dashboard,
        name="dashboard"
    ),



    # ==========================
    # LIST
    # ==========================

    path(
        "",
        views.equipment_list,
        name="list"
    ),



    # ==========================
    # CREATE
    # ==========================

    path(
        "add/",
        views.create_equipment,
        name="create"
    ),



    # ==========================
    # DETAIL
    # ==========================

    path(
        "<int:pk>/",
        views.equipment_detail,
        name="detail"
    ),



    # ==========================
    # UPDATE
    # ==========================

    path(
        "<int:pk>/edit/",
        views.update_equipment,
        name="update"
    ),



    # ==========================
    # DELETE
    # ==========================

    path(
        "<int:pk>/delete/",
        views.delete_equipment,
        name="delete"
    ),

]