from django.urls import path

from . import views


app_name = "equipment"


urlpatterns = [

    # Dashboard
    path(
        "dashboard/",
        views.equipment_dashboard,
        name="dashboard",
    ),


    # Equipment list
    path(
        "",
        views.equipment_list,
        name="list",
    ),


    # Add equipment
    path(
        "add/",
        views.equipment_create,
        name="create",
    ),


    # Equipment details
    path(
        "<int:pk>/",
        views.equipment_detail,
        name="detail",
    ),


    # Edit equipment
    path(
        "<int:pk>/edit/",
        views.equipment_update,
        name="update",
    ),


    # Delete equipment
    path(
        "<int:pk>/delete/",
        views.equipment_delete,
        name="delete",
    ),

]