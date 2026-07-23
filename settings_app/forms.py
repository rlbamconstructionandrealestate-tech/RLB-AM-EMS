from django import forms

from .models import (
    CompanyProfile,
    SystemPreference,
    NotificationSetting,
)



# =====================================================
# COMPANY PROFILE FORM
# =====================================================


class CompanyProfileForm(forms.ModelForm):


    class Meta:

        model = CompanyProfile


        fields = [

            "company_name",
            "short_name",
            "logo",
            "email",
            "phone",
            "website",
            "address",
            "city",
            "country",
            "tax_number",

        ]



        widgets = {


            "company_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Company Name",
                }
            ),



            "short_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short Name",
                }
            ),




            "logo": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),





            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),





            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                }
            ),






            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Website URL",
                }
            ),





            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Company Address",
                }
            ),





            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "City",
                }
            ),






            "country": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),





            "tax_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tax Identification Number",
                }
            ),


        }









# =====================================================
# SYSTEM PREFERENCE FORM
# =====================================================


class SystemPreferenceForm(forms.ModelForm):


    class Meta:

        model = SystemPreference


        fields = [

            "system_name",

            "enable_notifications",

            "enable_email",

            "enable_dark_mode",

            "maintenance_mode",

            "items_per_page",

        ]



        widgets = {


            "system_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),




            "items_per_page": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),




            "enable_notifications": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),





            "enable_email": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),





            "enable_dark_mode": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),





            "maintenance_mode": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),


        }









# =====================================================
# NOTIFICATION SETTINGS FORM
# =====================================================


class NotificationSettingForm(forms.ModelForm):


    class Meta:

        model = NotificationSetting


        fields = [

            "email_notifications",

            "project_updates",

            "payment_alerts",

            "equipment_alerts",

            "maintenance_alerts",

        ]



        widgets = {


            "email_notifications": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),



            "project_updates": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),



            "payment_alerts": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),



            "equipment_alerts": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),



            "maintenance_alerts": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),


        }