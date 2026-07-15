from django.urls import path
from . import views

app_name = "finance"

urlpatterns = [

    # Finance Dashboard
    path("", views.dashboard, name="dashboard"),


    # Income
    path("income/", views.income_list, name="income_list"),
    path("income/add/", views.add_income, name="add_income"),


    # Expenses
    path("expenses/", views.expense_list, name="expense_list"),
    path("expense/add/", views.add_expense, name="add_expense"),


    # Invoices
    path("invoices/", views.invoice_list, name="invoice_list"),
    path("invoice/add/", views.add_invoice, name="add_invoice"),


    # Reports
    path("reports/", views.reports, name="reports"),

]