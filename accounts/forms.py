from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)

from .models import User



# ======================================================
# LOGIN FORM
# ======================================================

class LoginForm(AuthenticationForm):

    remember_me = forms.BooleanField(

        required=False,

        label="Remember Me",

        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input"
            }
        )
    )


    class Meta:

        model = User

        fields = [
            "username",
            "password",
        ]



    def __init__(self, *args, **kwargs):

        super().__init__(
            *args,
            **kwargs
        )


        self.fields["username"].widget.attrs.update({

            "class":
            "form-control py-3 rounded-2",

            "placeholder":
            "Username",

            "autocomplete":
            "username",

        })


        self.fields["password"].widget.attrs.update({

            "class":
            "form-control py-3 rounded-2",

            "placeholder":
            "Password",

            "autocomplete":
            "current-password",

        })





# ======================================================
# PROFILE UPDATE FORM
# ======================================================

class UserProfileForm(forms.ModelForm):


    class Meta:

        model = User


        fields = [

            "first_name",

            "last_name",

            "email",

            "phone",

            "job_title",

            "department",

            "profile_picture",

        ]


        widgets = {


            "first_name":
            forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"First Name"
                }
            ),



            "last_name":
            forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Last Name"
                }
            ),



            "email":
            forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Email Address"
                }
            ),



            "phone":
            forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Phone Number"
                }
            ),



            "job_title":
            forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Job Title"
                }
            ),



            "department":
            forms.Select(
                attrs={
                    "class":"form-select"
                }
            ),



            "profile_picture":
            forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),

        }





# ======================================================
# CHANGE PASSWORD
# ======================================================

class CustomPasswordChangeForm(PasswordChangeForm):


    old_password = forms.CharField(

        label="Current Password",

        widget=forms.PasswordInput(

            attrs={

                "class":
                "form-control",

                "placeholder":
                "Current Password"

            }
        )
    )



    new_password1 = forms.CharField(

        label="New Password",

        widget=forms.PasswordInput(

            attrs={

                "class":
                "form-control",

                "placeholder":
                "New Password"

            }
        )
    )



    new_password2 = forms.CharField(

        label="Confirm Password",

        widget=forms.PasswordInput(

            attrs={

                "class":
                "form-control",

                "placeholder":
                "Confirm Password"

            }
        )
    )