from django.db import models
from django.utils import timezone


class Client(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("prospect", "Prospect"),
    ]

    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    industry = models.CharField(max_length=100, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["company_name"]
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.company_name


class Contract(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("active", "Active"),
        ("completed", "Completed"),
        ("expired", "Expired"),
        ("cancelled", "Cancelled"),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="contracts",
    )

    contract_number = models.CharField(
        max_length=50,
        unique=True,
    )

    project_name = models.CharField(max_length=200)

    total_value = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"

    def __str__(self):
        return f"{self.contract_number} - {self.client.company_name}"

    @property
    def days_remaining(self):
        return (self.end_date - timezone.now().date()).days

    @property
    def is_expired(self):
        return self.end_date < timezone.now().date()