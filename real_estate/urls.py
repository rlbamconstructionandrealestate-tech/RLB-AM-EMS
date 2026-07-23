from django.urls import path

from . import views


app_name = "real_estate"



urlpatterns = [

    # Real Estate Dashboard
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),


    # Property List
    path(
        "properties/",
        views.property_list,
        name="property_list"
    ),


    # Add Property
    path(
        "properties/create/",
        views.create_property,
        name="create_property"
    ),


    # Property Details
    path(
        "properties/<int:pk>/",
        views.property_detail,
        name="property_detail"
    ),


    # Sales
    path(
        "sales/",
        views.sales,
        name="sales"
    ),


    # Rentals
    path(
        "rentals/",
        views.rentals,
        name="rentals"
    ),

]