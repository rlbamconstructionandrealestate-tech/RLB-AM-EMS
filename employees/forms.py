from django import forms

from .models import Employee



class EmployeeForm(forms.ModelForm):


    class Meta:


        model = Employee


        fields = "__all__"



        widgets = {


            "date_of_birth": forms.DateInput(

                attrs={
                    "type":"date",
                    "class":"form-control"
                }

            ),



            "date_joined": forms.DateInput(

                attrs={
                    "type":"date",
                    "class":"form-control"
                }

            ),



            "address": forms.Textarea(

                attrs={
                    "rows":3,
                    "class":"form-control"
                }

            ),

        }



    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)


        for field in self.fields:

            if field not in [
                "profile_picture",
            ]:

                self.fields[field].widget.attrs.update(

                    {
                        "class":
                        "form-control"
                    }

                )