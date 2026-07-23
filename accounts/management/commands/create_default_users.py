from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


DEFAULT_USERS = [
    {
        "username": "owner",
        "password": "Owner@123",
        "first_name": "Managing",
        "last_name": "Director",
        "email": "owner@rlbam.co.tz",
        "employee_id": "EMP001",
        "role": "owner",
        "department": "management",
        "job_title": "Managing Director",
        "is_staff": True,
        "is_superuser": True,
    },
    {
        "username": "director",
        "password": "Director@123",
        "first_name": "Company",
        "last_name": "Director",
        "email": "director@rlbam.co.tz",
        "employee_id": "EMP002",
        "role": "director",
        "department": "management",
        "job_title": "Director",
        "is_staff": True,
        "is_superuser": False,
    },
    {
        "username": "manager",
        "password": "Manager@123",
        "first_name": "General",
        "last_name": "Manager",
        "email": "manager@rlbam.co.tz",
        "employee_id": "EMP003",
        "role": "manager",
        "department": "management",
        "job_title": "Manager",
        "is_staff": True,
        "is_superuser": False,
    },
    {
        "username": "secretary",
        "password": "Secretary@123",
        "first_name": "Office",
        "last_name": "Secretary",
        "email": "secretary@rlbam.co.tz",
        "employee_id": "EMP004",
        "role": "secretary",
        "department": "administration",
        "job_title": "Secretary",
        "is_staff": True,
        "is_superuser": False,
    },
]


class Command(BaseCommand):
    help = "Create the default enterprise user accounts."

    def handle(self, *args, **kwargs):

        for account in DEFAULT_USERS:

            username = account["username"]

            if User.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.WARNING(f"{username} already exists.")
                )
                continue

            user = User.objects.create_user(
                username=account["username"],
                email=account["email"],
                password=account["password"],
            )

            user.first_name = account["first_name"]
            user.last_name = account["last_name"]
            user.employee_id = account["employee_id"]
            user.role = account["role"]
            user.department = account["department"]
            user.job_title = account["job_title"]

            user.is_staff = account["is_staff"]
            user.is_superuser = account["is_superuser"]
            user.is_active = True
            user.is_active_employee = True

            user.save()

            self.stdout.write(
                self.style.SUCCESS(f"Created user: {username}")
            )

        self.stdout.write(
            self.style.SUCCESS("\nAll default users have been processed.")
        )