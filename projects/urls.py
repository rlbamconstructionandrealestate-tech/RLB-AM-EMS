from django.urls import path

from . import views



app_name = "projects"



urlpatterns = [

    # =====================================================
    # DASHBOARD
    # =====================================================

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),



    # =====================================================
    # PROJECT LIST
    # =====================================================

    path(
        "list/",
        views.project_list,
        name="list"
    ),



    # =====================================================
    # CREATE
    # =====================================================

    path(
        "create/",
        views.create_project,
        name="create"
    ),



    # =====================================================
    # DETAIL
    # =====================================================

    path(
        "<int:pk>/",
        views.project_detail,
        name="detail"
    ),



    # =====================================================
    # UPDATE
    # =====================================================

    path(
        "<int:pk>/edit/",
        views.edit_project,
        name="edit"
    ),



    # =====================================================
    # DELETE
    # =====================================================

    path(
        "<int:pk>/delete/",
        views.delete_project,
        name="delete"
    ),



    # =====================================================
    # MILESTONES
    # =====================================================

    path(
        "<int:pk>/milestone/add/",
        views.add_milestone,
        name="add_milestone"
    ),



    # =====================================================
    # EXPENSES
    # =====================================================

    path(
        "<int:pk>/expense/add/",
        views.add_expense,
        name="add_expense"
    ),

]