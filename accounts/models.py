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
        ("admin", "System Administrator"),
        ("manager", "General Manager"),
        ("director", "Board of Directors"),
        ("finance", "Finance Officer"),
        ("secretary", "Secretary / Accountant"),
        ("engineer", "Civil Engineer"),
        ("qs", "Quantity Surveyor"),
        ("equipment", "Equipment Officer"),
        ("fuel", "Fuel Officer"),
        ("project_manager", "Project Manager"),
        ("hr", "Human Resources Officer"),
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
        ("hr", "Human Resources"),
        ("administration", "Administration"),
    ]

    # ======================================================
    # EXTRA FIELDS
    # ======================================================
    employee_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=30,
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
    # PERMISSIONS
    # ======================================================
    @property
    def is_admin(self):
        return self.is_superuser or self.role == "admin"

    @property
    def is_manager(self):
        return self.role == "manager"

    @property
    def is_director(self):
        return self.role == "director"

    def can_access_finance(self):
        return self.role in [
            "admin",
            "manager",
            "finance",
            "secretary",
        ]

    def can_access_equipment(self):
        return self.role in [
            "admin",
            "manager",
            "equipment",
        ]

    def can_access_fuel(self):
        return self.role in [
            "admin",
            "manager",
            "fuel",
        ]

    def can_access_projects(self):
        return self.role in [
            "admin",
            "manager",
            "project_manager",
            "engineer",
            "qs",
        ]

    def can_access_hr(self):
        return self.role in [
            "admin",
            "manager",
            "hr",
        ]

    def can_access_real_estate(self):
        return self.role in [
            "admin",
            "manager",
        ]