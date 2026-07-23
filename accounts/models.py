from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User Model for RLB-AM Enterprise Management System
    """

    # ======================================================
    # ROLE CHOICES
    # ======================================================
    ROLE_CHOICES = [
        ("owner", "Managing Director"),
        ("director", "Director"),
        ("manager", "Manager"),
        ("secretary", "Secretary"),
    ]

    # ======================================================
    # DEPARTMENT CHOICES
    # ======================================================
    DEPARTMENT_CHOICES = [
        ("management", "Management"),
        ("finance", "Finance"),
        ("engineering", "Engineering"),
        ("projects", "Projects"),
        ("equipment", "Equipment"),
        ("fuel", "Fuel Management"),
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
        blank=True,
        null=True
    )

    job_title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    is_active_employee = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}".strip()
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    # ======================================================
    # ROLE HELPERS
    # ======================================================

    @property
    def is_owner(self):
        return self.role == "owner"

    @property
    def is_director(self):
        return self.role == "director"

    @property
    def is_manager(self):
        return self.role == "manager"

    @property
    def is_secretary(self):
        return self.role == "secretary"

    # ======================================================
    # PERMISSIONS
    # ======================================================

    def can_manage_users(self):
        return self.is_owner

    def can_manage_settings(self):
        return self.is_owner

    def can_access_employees(self):
        return self.role in [
            "owner",
            "manager",
        ]

    def can_access_finance(self):
        return self.role in [
            "owner",
            "manager",
            "secretary",
        ]

    def can_access_equipment(self):
        return self.role in [
            "owner",
            "manager",
            "secretary",
        ]

    def can_access_rentals(self):
        return self.role in [
            "owner",
            "manager",
            "secretary",
        ]

    def can_access_fuel(self):
        return self.role in [
            "owner",
            "manager",
            "secretary",
        ]

    def can_access_maintenance(self):
        return self.role in [
            "owner",
            "manager",
            "secretary",
        ]

    def can_access_projects(self):
        return self.role in [
            "owner",
            "manager",
            "secretary",
        ]

    def can_access_crm(self):
        return self.role in [
            "owner",
            "manager",
            "secretary",
        ]

    def can_access_documents(self):
        return self.role in [
            "owner",
            "manager",
            "secretary",
        ]

    def can_access_reports(self):
        return self.role in [
            "owner",
            "manager",
            "director",
        ]

    def is_read_only(self):
        return self.role == "director"