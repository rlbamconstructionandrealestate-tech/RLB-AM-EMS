from django import forms

from .models import Equipment, EquipmentCategory


class DateInput(forms.DateInput):
    input_type = "date"


class EquipmentCategoryForm(forms.ModelForm):
    class Meta:
        model = EquipmentCategory
        fields = [
            "name",
            "description",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Category Name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Description",
                }
            ),
        }


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment

        exclude = (
            "created_at",
            "updated_at",
        )

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Equipment Name",
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "asset_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "readonly": True,
                    "placeholder": "Auto Generated",
                }
            ),

            "registration_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "serial_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "engine_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "chassis_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "manufacturer": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "model": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "manufacture_year": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "ownership": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "fuel_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "hour_meter": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.1",
                }
            ),

            "purchase_date": DateInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "purchase_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "daily_rate": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "weekly_rate": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "monthly_rate": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "current_location": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "insurance_expiry": DateInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "road_license_expiry": DateInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "next_service_date": DateInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def clean_purchase_price(self):
        value = self.cleaned_data["purchase_price"]

        if value < 0:
            raise forms.ValidationError(
                "Purchase price cannot be negative."
            )

        return value

    def clean_daily_rate(self):
        value = self.cleaned_data["daily_rate"]

        if value < 0:
            raise forms.ValidationError(
                "Daily rate cannot be negative."
            )

        return value

    def clean_weekly_rate(self):
        value = self.cleaned_data["weekly_rate"]

        if value < 0:
            raise forms.ValidationError(
                "Weekly rate cannot be negative."
            )

        return value

    def clean_monthly_rate(self):
        value = self.cleaned_data["monthly_rate"]

        if value < 0:
            raise forms.ValidationError(
                "Monthly rate cannot be negative."
            )

        return value

    def clean_hour_meter(self):
        value = self.cleaned_data["hour_meter"]

        if value < 0:
            raise forms.ValidationError(
                "Hour meter cannot be negative."
            )

        return value