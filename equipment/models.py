from django.db import models
from django.urls import reverse


class EquipmentCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Equipment Category"
        verbose_name_plural = "Equipment Categories"

    def __str__(self):
        return self.name


class Equipment(models.Model):

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Working", "Working"),
        ("Rented", "Rented"),
        ("Maintenance", "Maintenance"),
        ("Out of Service", "Out of Service"),
    ]

    FUEL_CHOICES = [
        ("Diesel", "Diesel"),
        ("Petrol", "Petrol"),
        ("Electric", "Electric"),
        ("Hybrid", "Hybrid"),
        ("Other", "Other"),
    ]

    OWNERSHIP_CHOICES = [
        ("Company", "Company"),
        ("Leased", "Leased"),
        ("Hired", "Hired"),
    ]

    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        EquipmentCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="equipments",
    )

    asset_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
    )

    registration_number = models.CharField(
        max_length=50,
        blank=True,
    )

    serial_number = models.CharField(
        max_length=100,
        blank=True,
    )

    engine_number = models.CharField(
        max_length=100,
        blank=True,
    )

    chassis_number = models.CharField(
        max_length=100,
        blank=True,
    )

    manufacturer = models.CharField(
        max_length=100,
        blank=True,
    )

    model = models.CharField(
        max_length=100,
        blank=True,
    )

    manufacture_year = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    ownership = models.CharField(
        max_length=20,
        choices=OWNERSHIP_CHOICES,
        default="Company",
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES,
        default="Diesel",
    )

    hour_meter = models.DecimalField(
        max_digits=12,
        decimal_places=1,
        default=0,
    )

    purchase_date = models.DateField(
        null=True,
        blank=True,
    )

    purchase_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )

    daily_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    weekly_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    monthly_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    current_location = models.CharField(
        max_length=200,
        blank=True,
    )

    insurance_expiry = models.DateField(
        null=True,
        blank=True,
    )

    road_license_expiry = models.DateField(
        null=True,
        blank=True,
    )

    next_service_date = models.DateField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Available",
    )

    image = models.ImageField(
        upload_to="equipment/",
        blank=True,
        null=True,
    )

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"

    def save(self, *args, **kwargs):

        if not self.asset_number:

            last = Equipment.objects.order_by("-id").first()

            if last:
                number = last.id + 1
            else:
                number = 1

            self.asset_number = f"EQ-{number:05d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.asset_number} - {self.name}"

    def get_absolute_url(self):
        return reverse(
            "equipment:detail",
            kwargs={"pk": self.pk},
        )