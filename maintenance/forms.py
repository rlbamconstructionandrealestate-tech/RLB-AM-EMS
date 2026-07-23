from django import forms

from .models import MaintenanceRecord



class MaintenanceRecordForm(forms.ModelForm):


    class Meta:

        model = MaintenanceRecord


        fields = [

            "equipment",

            "title",

            "description",

            "service_date",

            "next_service_date",

            "technician",

            "cost",

            "status",

        ]



        widgets = {


            "equipment": forms.Select(

                attrs={

                    "class": "form-select"

                }

            ),



            "title": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder":
                    "Maintenance title"

                }

            ),



            "description": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 4,

                    "placeholder":
                    "Describe maintenance work..."

                }

            ),



            "service_date": forms.DateInput(

                attrs={

                    "class": "form-control",

                    "type": "date"

                }

            ),



            "next_service_date": forms.DateInput(

                attrs={

                    "class": "form-control",

                    "type": "date"

                }

            ),



            "technician": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder":
                    "Technician name"

                }

            ),



            "cost": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "placeholder":
                    "Maintenance cost"

                }

            ),



            "status": forms.Select(

                attrs={

                    "class": "form-select"

                }

            ),

        }