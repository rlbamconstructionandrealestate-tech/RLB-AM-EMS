from django.urls import path

from . import views


app_name = "documents"



urlpatterns = [

    # Documents Dashboard
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),



    # Document List
    path(
        "list/",
        views.document_list,
        name="list"
    ),



    # Upload Document
    path(
        "upload/",
        views.upload_document,
        name="upload"
    ),



    # Document Details
    path(
        "<int:pk>/",
        views.document_detail,
        name="detail"
    ),



    # Delete Document
    path(
        "<int:pk>/delete/",
        views.delete_document,
        name="delete"
    ),

]