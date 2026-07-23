from django.db import models
from django.utils import timezone



class Equipment(models.Model):


    STATUS_CHOICES = [

        ("available", "Available"),

        ("working", "Working"),

        ("maintenance", "Under Maintenance"),

        ("inactive", "Inactive"),

    ]



    asset_number = models.CharField(
        max_length=50,
        unique=True
    )


    name = models.CharField(
        max_length=150
    )


    category = models.CharField(
        max_length=100
    )


    manufacturer = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    model = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available"
    )


    current_location = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )



    purchase_date = models.DateField(
        blank=True,
        null=True
    )



    purchase_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )



    current_value = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )



    image = models.ImageField(
        upload_to="equipment/",
        blank=True,
        null=True
    )



    description = models.TextField(
        blank=True,
        null=True
    )



    # Maintenance preparation

    last_service_date = models.DateField(
        blank=True,
        null=True
    )


    next_service_date = models.DateField(
        blank=True,
        null=True
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


        verbose_name = "Equipment"

        verbose_name_plural = "Equipment"



    def __str__(self):

        return f"{self.asset_number} - {self.name}"




    @property
    def age_years(self):

        if self.purchase_date:

            today = timezone.now().date()

            return today.year - self.purchase_date.year


        return 0