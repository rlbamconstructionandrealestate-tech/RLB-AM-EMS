from django import forms

from .models import (
    Project,
    ProjectMilestone,
    ProjectExpense
)



# =====================================================
# PROJECT FORM
# =====================================================


class ProjectForm(forms.ModelForm):


    class Meta:


        model = Project


        fields = [

            "project_code",

            "name",

            "description",

            "client",

            "location",

            "manager",

            "status",

            "priority",

            "progress",

            "contract_value",

            "amount_paid",

            "start_date",

            "end_date",

        ]



        widgets = {


            "project_code": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Example: RLB-001"

                }

            ),



            "name": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Project name"

                }

            ),



            "description": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 4,

                    "placeholder": "Project description"

                }

            ),



            "client": forms.Select(

                attrs={

                    "class": "form-select"

                }

            ),



            "location": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Project location"

                }

            ),



            "manager": forms.Select(

                attrs={

                    "class": "form-select"

                }

            ),



            "status": forms.Select(

                attrs={

                    "class": "form-select"

                }

            ),



            "priority": forms.Select(

                attrs={

                    "class": "form-select"

                }

            ),



            "progress": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "min": 0,

                    "max": 100,

                    "placeholder": "0 - 100"

                }

            ),



            "contract_value": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Contract amount"

                }

            ),



            "amount_paid": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Amount paid"

                }

            ),



            "start_date": forms.DateInput(

                attrs={

                    "class": "form-control",

                    "type": "date"

                }

            ),



            "end_date": forms.DateInput(

                attrs={

                    "class": "form-control",

                    "type": "date"

                }

            ),


        }





# =====================================================
# PROJECT MILESTONE FORM
# =====================================================


class ProjectMilestoneForm(forms.ModelForm):


    class Meta:


        model = ProjectMilestone


        fields = [

            "name",

            "description",

            "due_date",

            "status",

        ]



        widgets = {


            "name": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Milestone name"

                }

            ),



            "description": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 3

                }

            ),



            "due_date": forms.DateInput(

                attrs={

                    "class": "form-control",

                    "type": "date"

                }

            ),



            "status": forms.Select(

                attrs={

                    "class": "form-select"

                }

            ),


        }






# =====================================================
# PROJECT EXPENSE FORM
# =====================================================


class ProjectExpenseForm(forms.ModelForm):


    class Meta:


        model = ProjectExpense


        fields = [

            "category",

            "description",

            "amount",

        ]



        widgets = {


            "category": forms.Select(

                attrs={

                    "class": "form-select"

                }

            ),



            "description": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Expense description"

                }

            ),



            "amount": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Amount"

                }

            ),


        }