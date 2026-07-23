from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



# =====================================================
# PROJECT MODEL
# =====================================================

class Project(models.Model):


    STATUS_CHOICES = (

        ("planning", "Planning"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("on_hold", "On Hold"),
        ("cancelled", "Cancelled"),

    )


    PRIORITY_CHOICES = (

        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("urgent", "Urgent"),

    )



    # BASIC INFORMATION


    project_code = models.CharField(
        max_length=50,
        unique=True
    )


    name = models.CharField(
        max_length=200
    )


    description = models.TextField(
        blank=True,
        null=True
    )



    # CLIENT


    client = models.ForeignKey(
        "crm.Client",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projects"
    )



    # LOCATION


    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )



    # MANAGEMENT


    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_projects"
    )


    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="planning"
    )


    priority = models.CharField(
        max_length=30,
        choices=PRIORITY_CHOICES,
        default="medium"
    )



    progress = models.PositiveIntegerField(
        default=0,
        help_text="Project completion percentage"
    )



    # FINANCE


    contract_value = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )


    amount_paid = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )



    # DATES


    start_date = models.DateField(
        blank=True,
        null=True
    )


    end_date = models.DateField(
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

        ordering = [
            "-created_at"
        ]



    def __str__(self):

        return f"{self.project_code} - {self.name}"




    # CALCULATIONS


    @property
    def balance(self):

        return self.contract_value - self.amount_paid



    @property
    def total_expenses(self):

        return self.expenses.aggregate(

            total=models.Sum("amount")

        )["total"] or 0



    @property
    def profit(self):

        return self.contract_value - self.total_expenses



    @property
    def client_name_display(self):

        if self.client:

            return self.client.company_name

        return "-"





# =====================================================
# PROJECT MILESTONE
# =====================================================


class ProjectMilestone(models.Model):


    STATUS_CHOICES = (

        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("delayed", "Delayed"),

    )



    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="milestones"
    )



    name = models.CharField(
        max_length=200
    )


    description = models.TextField(
        blank=True,
        null=True
    )


    due_date = models.DateField(
        blank=True,
        null=True
    )


    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="pending"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    class Meta:

        ordering = [
            "due_date"
        ]



    def __str__(self):

        return self.name






# =====================================================
# PROJECT EXPENSE
# =====================================================


class ProjectExpense(models.Model):


    CATEGORY_CHOICES = (

        ("material", "Materials"),
        ("labor", "Labor"),
        ("fuel", "Fuel"),
        ("transport", "Transport"),
        ("equipment", "Equipment"),
        ("other", "Other"),

    )



    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="expenses"
    )



    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other"
    )



    description = models.CharField(
        max_length=255
    )



    amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )



    date = models.DateField(
        auto_now_add=True
    )



    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="project_expenses"
    )



    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    class Meta:

        ordering = [
            "-date"
        ]



    def __str__(self):

        return f"{self.project.name} - {self.amount}"







# =====================================================
# PROJECT ACTIVITY LOG
# =====================================================


class ProjectActivity(models.Model):


    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="activities"
    )


    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="project_activities"
    )


    message = models.TextField()



    created_at = models.DateTimeField(
        auto_now_add=True
    )



    class Meta:

        ordering = [
            "-created_at"
        ]



    def __str__(self):

        return self.message[:50]