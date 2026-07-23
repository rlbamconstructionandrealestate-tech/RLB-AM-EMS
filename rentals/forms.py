from django import forms

from .models import Rental



class RentalForm(forms.ModelForm):


    class Meta:

        model = Rental


        fields = [

            "client_name",
            "client_phone",
            "equipment",
            "start_date",
            "end_date",
            "daily_rate",
            "total_amount",
            "status",
            "notes",

        ]


        widgets = {


            "start_date": forms.DateInput(

                attrs={
                    "type": "date",
                    "class": "form-control"
                }

            ),


            "end_date": forms.DateInput(

                attrs={
                    "type": "date",
                    "class": "form-control"
                }

            ),


            "notes": forms.Textarea(

                attrs={
                    "rows":4,
                    "class":"form-control"
                }

            )

        }



    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)


        for field in self.fields.values():

            field.widget.attrs.update({

                "class":"form-control"

            })