from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



# =====================================================
# EMPLOYEE MODEL
# =====================================================

class Employee(models.Model):


    # =====================================================
    # CHOICES
    # =====================================================

    EMPLOYMENT_STATUS = (

        ("active", "Active"),

        ("inactive", "Inactive"),

        ("leave", "On Leave"),

        ("terminated", "Terminated"),

    )



    EMPLOYEE_TYPE = (

        ("management", "Management"),

        ("engineering", "Engineering"),

        ("technical", "Technical"),

        ("operator", "Machine Operator"),

        ("driver", "Driver"),

        ("office", "Office Staff"),

        ("casual", "Casual Worker"),

        ("contract", "Contract"),

        ("intern", "Intern"),

        ("permanent", "Permanent"),

    )



    # =====================================================
    # USER CONNECTION
    # =====================================================


    user = models.OneToOneField(

        User,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="employee_profile"

    )



    # =====================================================
    # PERSONAL INFORMATION
    # =====================================================


    employee_id = models.CharField(

        max_length=50,

        unique=True

    )



    first_name = models.CharField(

        max_length=100

    )



    last_name = models.CharField(

        max_length=100

    )



    gender = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )



    phone = models.CharField(

        max_length=30,

        blank=True,

        null=True

    )



    email = models.EmailField(

        blank=True,

        null=True

    )



    photo = models.ImageField(

        upload_to="employees/",

        blank=True,

        null=True

    )




    # =====================================================
    # EMPLOYMENT INFORMATION
    # =====================================================


    position = models.CharField(

        max_length=150

    )



    department = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )



    employee_type = models.CharField(

        max_length=50,

        choices=EMPLOYEE_TYPE,

        default="office"

    )



    status = models.CharField(

        max_length=50,

        choices=EMPLOYMENT_STATUS,

        default="active"

    )



    date_joined = models.DateField()




    # =====================================================
    # FINANCIAL INFORMATION
    # =====================================================


    salary = models.DecimalField(

        max_digits=12,

        decimal_places=2,

        default=0

    )



    bank_name = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )



    bank_account = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )




    # =====================================================
    # EMERGENCY CONTACT
    # =====================================================


    emergency_contact = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )



    emergency_phone = models.CharField(

        max_length=30,

        blank=True,

        null=True

    )




    # =====================================================
    # SYSTEM TRACKING
    # =====================================================


    created_at = models.DateTimeField(

        auto_now_add=True

    )



    updated_at = models.DateTimeField(

        auto_now=True

    )




    # =====================================================
    # META
    # =====================================================


    class Meta:

        ordering = [

            "first_name"

        ]

        verbose_name = "Employee"

        verbose_name_plural = "Employees"




    # =====================================================
    # METHODS
    # =====================================================


    def __str__(self):

        return f"{self.first_name} {self.last_name} ({self.employee_id})"



    @property

    def full_name(self):

        return f"{self.first_name} {self.last_name}"