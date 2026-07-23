from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.utils import timezone

from equipment.models import Equipment
from employees.models import Employee
from rentals.models import Rental
from projects.models import Project
from maintenance.models import MaintenanceRecord
from finance.models import Income



@login_required
def dashboard(request):


    today = timezone.now()


    current_month = today.month

    current_year = today.year



    # ==============================
    # KPI DATA
    # ==============================


    total_equipment = (
        Equipment.objects.count()
    )



    available_equipment = (
        Equipment.objects.filter(
            status="available"
        ).count()
    )



    total_employees = (
        Employee.objects.count()
    )



    active_rentals = (
        Rental.objects.filter(
            status="active"
        ).count()
    )



    active_projects = (
        Project.objects.filter(
            status="active"
        ).count()
    )



    maintenance_due = (
        MaintenanceRecord.objects.filter(
            status="pending"
        ).count()
    )





    # ==============================
    # MONTHLY REVENUE
    # ==============================


    monthly_revenue = (

        Income.objects.filter(

            date_received__month=current_month,

            date_received__year=current_year

        )

        .aggregate(

            total=Sum("amount")

        )

        ["total"] or 0

    )





    # ==============================
    # REVENUE CHART DATA
    # ==============================


    revenue_data = (

        Income.objects

        .filter(

            date_received__year=current_year

        )

        .annotate(

            month=TruncMonth(
                "date_received"
            )

        )

        .values(
            "month"
        )

        .annotate(

            total=Sum(
                "amount"
            )

        )

        .order_by(
            "month"
        )

    )



    revenue_months = []

    revenue_values = []



    for item in revenue_data:


        revenue_months.append(

            item["month"].strftime("%b")

        )


        revenue_values.append(

            float(
                item["total"]
            )

        )





    context = {


        # ==============================
        # KPI
        # ==============================


        "total_equipment":
            total_equipment,


        "available_equipment":
            available_equipment,


        "total_employees":
            total_employees,


        "active_rentals":
            active_rentals,


        "monthly_revenue":
            monthly_revenue,



        # ==============================
        # STATUS
        # ==============================


        "active_projects":
            active_projects,


        "maintenance_due":
            maintenance_due,



        # ==============================
        # CHART
        # ==============================


        "revenue_months":
            revenue_months,


        "revenue_values":
            revenue_values,


        "current_year":
            current_year,


    }



    return render(

        request,

        "dashboard/dashboard.html",

        context

    )