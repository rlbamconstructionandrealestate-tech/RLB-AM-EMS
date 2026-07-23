from django.urls import path

from . import views


app_name = "maintenance"



urlpatterns = [

    # Dashboard
    path(
        "dashboard/",
        views.maintenance_dashboard,
        name="dashboard"
    ),


    # Maintenance list
    path(
        "",
        views.maintenance_list,
        name="list"
    ),


    # Add maintenance
    path(
        "add/",
        views.maintenance_create,
        name="create"
    ),


    # Details
    path(
        "<int:pk>/",
        views.maintenance_detail,
        name="detail"
    ),


    # Edit
    path(
        "<int:pk>/edit/",
        views.maintenance_update,
        name="update"
    ),


    # Delete
    path(
        "<int:pk>/delete/",
        views.maintenance_delete,
        name="delete"
    ),

]