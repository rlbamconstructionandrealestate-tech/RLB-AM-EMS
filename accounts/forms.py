from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm
)

from .models import User


# ======================================================
# LOGIN FORM
# ======================================================

class LoginForm(AuthenticationForm):

    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input"
            }
        ),
        label="Remember Me"
    )


    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({

            "class": "form-control py-3 rounded-2xl",
            "placeholder": "Username",
            "autocomplete": "username"

        })


        self.fields["password"].widget.attrs.update({

            "class": "form-control py-3 rounded-2xl",
            "placeholder": "Password",
            "autocomplete": "current-password",
            "id": "id_password"

        })



# ======================================================
# REGISTRATION FORM
# ======================================================

class RegisterForm(UserCreationForm):


    first_name = forms.CharField(

        required=True,

        widget=forms.TextInput(attrs={

            "class": "form-control",
            "placeholder": "First Name"

        })

    )


    last_name = forms.CharField(

        required=True,

        widget=forms.TextInput(attrs={

            "class": "form-control",
            "placeholder": "Last Name"

        })

    )


    email = forms.EmailField(

        required=True,

        widget=forms.EmailInput(attrs={

            "class": "form-control",
            "placeholder": "Email Address"

        })

    )


    employee_id = forms.CharField(

        required=False,

        widget=forms.TextInput(attrs={

            "class": "form-control",
            "placeholder": "Employee ID"

        })

    )


    role = forms.ChoiceField(

        choices=User.ROLE_CHOICES,

        widget=forms.Select(attrs={

            "class": "form-control"

        })

    )


    department = forms.ChoiceField(

        choices=User.DEPARTMENT_CHOICES,

        required=False,

        widget=forms.Select(attrs={

            "class": "form-control"

        })

    )


    job_title = forms.CharField(

        required=False,

        widget=forms.TextInput(attrs={

            "class": "form-control",
            "placeholder": "Job Title"

        })

    )


    phone = forms.CharField(

        required=False,

        widget=forms.TextInput(attrs={

            "class": "form-control",
            "placeholder": "Phone Number"

        })

    )


    class Meta:

        model = User

        fields = [

            "first_name",
            "last_name",
            "username",
            "email",
            "employee_id",
            "role",
            "department",
            "job_title",
            "phone",
            "password1",
            "password2",

        ]


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            if "class" not in field.widget.attrs:

                field.widget.attrs.update({

                    "class": "form-control"

                })



# ======================================================
# PROFILE EDIT FORM
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



    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({

                "class": "form-control"

            })



# ======================================================
# CHANGE PASSWORD FORM
# ======================================================

class CustomPasswordChangeForm(PasswordChangeForm):


    old_password = forms.CharField(

        widget=forms.PasswordInput(attrs={

            "class": "form-control",
            "placeholder": "Current Password"

        })

    )


    new_password1 = forms.CharField(

        widget=forms.PasswordInput(attrs={

            "class": "form-control",
            "placeholder": "New Password"

        })

    )


    new_password2 = forms.CharField(

        widget=forms.PasswordInput(attrs={

            "class": "form-control",
            "placeholder": "Confirm New Password"

        })

    )