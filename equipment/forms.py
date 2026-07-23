from django import forms

from .models import Equipment



class EquipmentForm(forms.ModelForm):


    class Meta:


        model = Equipment


        fields = [

            "asset_number",
            "name",
            "category",
            "manufacturer",
            "model",
            "status",
            "current_location",
            "purchase_price",
            "purchase_date",
            "current_value",
            "image",
            "description",

        ]



        widgets = {


            "asset_number": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Asset Number"
                }
            ),



            "name": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Equipment Name"
                }
            ),



            "category": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Category"
                }
            ),



            "manufacturer": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Manufacturer"
                }
            ),



            "model": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Model"
                }
            ),



            "status": forms.Select(
                attrs={
                    "class":"form-select"
                }
            ),



            "current_location": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Current Location"
                }
            ),



            "purchase_price": forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Purchase Price"
                }
            ),



            "current_value": forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Current Value"
                }
            ),



            "purchase_date": forms.DateInput(
                attrs={
                    "class":"form-control",
                    "type":"date"
                }
            ),



            "image": forms.ClearableFileInput(
                attrs={
                    "class":"form-control"
                }
            ),



            "description": forms.Textarea(
                attrs={
                    "class":"form-control",
                    "rows":5,
                    "placeholder":"Equipment description..."
                }
            ),

        }




    def clean_asset_number(self):


        asset_number = self.cleaned_data.get(
            "asset_number"
        )


        if asset_number:

            return asset_number.upper()



        return asset_number