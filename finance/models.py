from django.db import models
from django.utils import timezone



class Income(models.Model):

    title = models.CharField(
        max_length=200
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    source = models.CharField(
        max_length=200
    )

    date_received = models.DateField(
        default=timezone.now
    )

    description = models.TextField(
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title





class Expense(models.Model):

    title = models.CharField(
        max_length=200
    )


    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    category = models.CharField(
        max_length=100
    )


    date_paid = models.DateField(
        default=timezone.now
    )


    description = models.TextField(
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title





class Invoice(models.Model):

    invoice_number = models.CharField(
        max_length=50,
        unique=True
    )


    client_name = models.CharField(
        max_length=200
    )


    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    status_choices = [

        ("Pending","Pending"),
        ("Paid","Paid"),
        ("Cancelled","Cancelled"),

    ]


    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default="Pending"
    )


    issue_date = models.DateField(
        default=timezone.now
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.invoice_number