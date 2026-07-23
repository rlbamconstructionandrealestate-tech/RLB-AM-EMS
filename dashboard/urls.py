from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "owner/",
        views.owner_dashboard,
        name="owner_dashboard"
    ),

    path(
        "director/",
        views.director_dashboard,
        name="director_dashboard"
    ),

    path(
        "manager/",
        views.manager_dashboard,
        name="manager_dashboard"
    ),

    path(
        "secretary/",
        views.secretary_dashboard,
        name="secretary_dashboard"
    ),

]