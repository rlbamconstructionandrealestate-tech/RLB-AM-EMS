from django import forms
from .models import Income, Expense, Invoice


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [
            "title",
            "amount",
            "source",
            "date_received",
            "description",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Income title",
            }),
            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "0.00",
            }),
            "source": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Income source",
            }),
            "date_received": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Description (optional)",
            }),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            "title",
            "amount",
            "category",
            "date_paid",
            "description",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Expense title",
            }),
            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "0.00",
            }),
            "category": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Category",
            }),
            "date_paid": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Description (optional)",
            }),
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "invoice_number",
            "client_name",
            "amount",
            "status",
            "issue_date",
        ]

        widgets = {
            "invoice_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Invoice Number",
            }),
            "client_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Client Name",
            }),
            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "0.00",
            }),
            "status": forms.Select(attrs={
                "class": "form-select",
            }),
            "issue_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
            }),
        }