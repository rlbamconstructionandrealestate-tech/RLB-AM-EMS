from django.contrib import admin
from .models import Income, Expense, Invoice



@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "amount",
        "source",
        "date_received",
    )




@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "amount",
        "category",
        "date_paid",
    )




@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):

    list_display = (
        "invoice_number",
        "client_name",
        "amount",
        "status",
        "issue_date",
    )