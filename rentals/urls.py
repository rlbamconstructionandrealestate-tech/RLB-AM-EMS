from django.urls import path

from . import views


app_name = "rentals"



urlpatterns = [


    # Dashboard
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),



    # Rental List
    path(
        "list/",
        views.rental_list,
        name="list"
    ),



    # Create Rental
    path(
        "create/",
        views.rental_create,
        name="create"
    ),



    # Rental Detail
    path(
        "detail/<int:pk>/",
        views.rental_detail,
        name="detail"
    ),



    # Update Rental
    path(
        "update/<int:pk>/",
        views.rental_update,
        name="update"
    ),



    # Delete Rental
    path(
        "delete/<int:pk>/",
        views.rental_delete,
        name="delete"
    ),


]