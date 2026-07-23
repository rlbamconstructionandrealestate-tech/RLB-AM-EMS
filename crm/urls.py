from django.urls import path
from . import views

app_name = "crm"

urlpatterns = [

    # ==========================
    # CRM Dashboard
    # ==========================
    path(
        "",
        views.dashboard,
        name="dashboard",
    ),

    # ==========================
    # Clients
    # ==========================
    path(
        "clients/",
        views.client_list,
        name="clients",
    ),

    path(
        "clients/create/",
        views.create_client,
        name="create_client",
    ),

    path(
        "clients/<int:pk>/",
        views.client_detail,
        name="client_detail",
    ),

    # ==========================
    # Contracts
    # ==========================
    path(
        "contracts/create/",
        views.create_contract,
        name="create_contract",
    ),

    path(
        "contracts/",
        views.contracts,
        name="contracts",
    ),

]