from decimal import Decimal

from django.db import models


class FuelRecord(models.Model):

    FUEL_TYPES = [
        ("Diesel", "Diesel"),
        ("Petrol", "Petrol"),
    ]

    PAYMENT_METHODS = [
        ("Cash", "Cash"),
        ("Bank", "Bank"),
        ("Mobile Money", "Mobile Money"),
        ("Credit", "Credit"),
    ]

    date = models.DateField()

    machine = models.ForeignKey(
        "equipment.Equipment",
        on_delete=models.CASCADE,
        related_name="fuel_records",
    )

    operator = models.CharField(max_length=100)

    project = models.CharField(
        max_length=150,
        blank=True,
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_TYPES,
        default="Diesel",
    )

    fuel_station = models.CharField(max_length=150)

    litres = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    price_per_litre = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    total_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        editable=False,
        default=0,
    )

    meter_reading = models.DecimalField(
        max_digits=12,
        decimal_places=1,
        null=True,
        blank=True,
    )

    receipt_number = models.CharField(
        max_length=100,
        blank=True,
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHODS,
        default="Cash",
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-id"]
        verbose_name = "Fuel Record"
        verbose_name_plural = "Fuel Records"

    def save(self, *args, **kwargs):
        self.total_cost = (
            Decimal(self.litres)
            * Decimal(self.price_per_litre)
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.machine} | {self.date}"