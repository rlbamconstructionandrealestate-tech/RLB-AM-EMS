from django import forms

from .models import FuelRecord


class FuelRecordForm(forms.ModelForm):

    class Meta:

        model = FuelRecord

        fields = [
            "date",
            "machine",
            "operator",
            "project",
            "fuel_type",
            "fuel_station",
            "litres",
            "price_per_litre",
            "meter_reading",
            "payment_method",
            "receipt_number",
            "notes",
        ]

        widgets = {

            "date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "notes": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),
        }