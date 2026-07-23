from django.db import models
from django.conf import settings

from equipment.models import Equipment



class Rental(models.Model):


    STATUS_CHOICES = [

        ("pending", "Pending"),
        ("active", "Active"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),

    ]


    # ==============================
    # CLIENT INFORMATION
    # ==============================

    client_name = models.CharField(
        max_length=200
    )


    client_phone = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )


    # ==============================
    # EQUIPMENT
    # ==============================

    equipment = models.ForeignKey(

        Equipment,

        on_delete=models.PROTECT,

        related_name="rentals"

    )


    # ==============================
    # RENTAL PERIOD
    # ==============================

    start_date = models.DateField()


    end_date = models.DateField()



    # ==============================
    # FINANCE
    # ==============================

    daily_rate = models.DecimalField(

        max_digits=12,

        decimal_places=2,

        default=0

    )


    total_amount = models.DecimalField(

        max_digits=12,

        decimal_places=2,

        default=0

    )



    # ==============================
    # STATUS
    # ==============================

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="pending"

    )



    notes = models.TextField(

        blank=True,

        null=True

    )



    created_by = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.SET_NULL,

        null=True,

        blank=True

    )



    created_at = models.DateTimeField(

        auto_now_add=True

    )


    updated_at = models.DateTimeField(

        auto_now=True

    )



    class Meta:

        ordering = [
            "-created_at"
        ]



    def __str__(self):

        return f"{self.client_name} - {self.equipment}"