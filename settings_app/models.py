from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



# =====================================================
# COMPANY PROFILE SETTINGS
# =====================================================

class CompanyProfile(models.Model):


    company_name = models.CharField(
        max_length=200,
        default="RLB-AM Construction & Real Estate Ltd"
    )


    short_name = models.CharField(
        max_length=100,
        default="RLB-AM"
    )


    logo = models.ImageField(
        upload_to="company/",
        blank=True,
        null=True
    )


    email = models.EmailField(
        blank=True,
        null=True
    )


    phone = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )


    website = models.URLField(
        blank=True,
        null=True
    )


    address = models.TextField(
        blank=True,
        null=True
    )


    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    country = models.CharField(
        max_length=100,
        default="Tanzania"
    )


    tax_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    class Meta:

        verbose_name = "Company Profile"

        verbose_name_plural = "Company Profile"



    def __str__(self):

        return self.company_name






# =====================================================
# SYSTEM PREFERENCES
# =====================================================

class SystemPreference(models.Model):


    system_name = models.CharField(
        max_length=100,
        default="RLB-AM EMS"
    )


    enable_notifications = models.BooleanField(
        default=True
    )


    enable_email = models.BooleanField(
        default=True
    )


    enable_dark_mode = models.BooleanField(
        default=False
    )


    maintenance_mode = models.BooleanField(
        default=False
    )


    items_per_page = models.PositiveIntegerField(
        default=25
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    class Meta:

        verbose_name = "System Preference"

        verbose_name_plural = "System Preferences"



    def __str__(self):

        return self.system_name








# =====================================================
# USER NOTIFICATION SETTINGS
# =====================================================

class NotificationSetting(models.Model):


    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE,

        related_name="notification_settings"

    )



    email_notifications = models.BooleanField(
        default=True
    )



    project_updates = models.BooleanField(
        default=True
    )



    payment_alerts = models.BooleanField(
        default=True
    )



    equipment_alerts = models.BooleanField(
        default=True
    )



    maintenance_alerts = models.BooleanField(
        default=True
    )



    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    class Meta:

        verbose_name = "Notification Setting"

        verbose_name_plural = "Notification Settings"



    def __str__(self):

        return f"{self.user.username} Settings"