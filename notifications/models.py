from django.db import models
from django.conf import settings


class Notification(models.Model):

    TYPE_CHOICES = [
        ("info", "Information"),
        ("success", "Success"),
        ("warning", "Warning"),
        ("danger", "Danger"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(
        max_length=200
    )

    message = models.TextField()


    notification_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="info"
    )


    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="medium"
    )


    is_read = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = [
            "-created_at"
        ]


    def __str__(self):
        return f"{self.user.username} - {self.title}"