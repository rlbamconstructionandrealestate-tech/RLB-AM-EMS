from django import forms
from .models import Client, Contract


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "company_name",
            "contact_person",
            "email",
            "phone",
            "address",
            "industry",
            "status",
            "notes",
        ]

        widgets = {
            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name"
            }),

            "contact_person": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Contact Person"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Company Address"
            }),

            "industry": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Industry"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "notes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Additional Notes"
            }),
        }


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "client",
            "contract_number",
            "project_name",
            "total_value",
            "start_date",
            "end_date",
            "status",
            "description",
        ]

        widgets = {
            "client": forms.Select(attrs={
                "class": "form-select"
            }),

            "contract_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "CTR-0001"
            }),

            "project_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Project Name"
            }),

            "total_value": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),

            "start_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "end_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Contract Description"
            }),
        }