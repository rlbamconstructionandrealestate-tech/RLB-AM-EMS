from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User Model for RLB-AM Enterprise Management System
    """

    ROLE_CHOICES = [
        ("manager", "Manager"),
        ("secretary", "Secretary / Accountant"),
        ("director", "Board of Directors"),
        ("qs", "Quantity Surveyor"),
        ("engineer", "Civil Engineer"),
    ]

    DEPARTMENT_CHOICES = [
        ("management", "Management"),
        ("finance", "Finance"),
        ("engineering", "Engineering"),
        ("real_estate", "Real Estate"),
        ("administration", "Administration"),
    ]

    employee_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="secretary"
    )

    department = models.CharField(
        max_length=30,
        choices=DEPARTMENT_CHOICES,
        blank=True
    )

    job_title = models.CharField(
        max_length=100,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    is_active_employee = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()