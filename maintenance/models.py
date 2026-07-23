from django.db import models
from equipment.models import Equipment



class MaintenanceRecord(models.Model):


    STATUS_CHOICES = [

        ("scheduled", "Scheduled"),

        ("completed", "Completed"),

        ("pending", "Pending"),

    ]



    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="maintenance_records"
    )


    title = models.CharField(
        max_length=150
    )


    description = models.TextField(
        blank=True,
        null=True
    )


    service_date = models.DateField()



    next_service_date = models.DateField(
        blank=True,
        null=True
    )



    technician = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )



    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )



    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="scheduled"
    )



    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    class Meta:

        ordering = [
            "-service_date"
        ]



    def __str__(self):

        return f"{self.equipment.name} - {self.title}"
    
Maintenance = MaintenanceRecord