from django.urls import path

from . import views

app_name = "fuel"

urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard",
    ),

    path(
        "records/",
        views.fuel_list,
        name="list",
    ),

    path(
        "add/",
        views.fuel_create,
        name="add",
    ),

    path(
        "<int:pk>/",
        views.fuel_detail,
        name="detail",
    ),

    path(
        "<int:pk>/edit/",
        views.fuel_update,
        name="edit",
    ),

    path(
        "<int:pk>/delete/",
        views.fuel_delete,
        name="delete",
    ),

]