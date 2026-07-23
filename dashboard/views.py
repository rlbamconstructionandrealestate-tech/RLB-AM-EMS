from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.utils import timezone


from equipment.models import Equipment
from employees.models import Employee
from rentals.models import Rental
from projects.models import Project
from maintenance.models import MaintenanceRecord
from finance.models import Income, Expense




# ======================================================
# COMMON DASHBOARD DATA
# ======================================================


def dashboard_context(request):


    today = timezone.now()


    current_month = today.month
    current_year = today.year



    context = {



        # USER

        "current_user":
            request.user,



        # EQUIPMENT

        "total_equipment":
            Equipment.objects.count(),



        "available_equipment":
            Equipment.objects.filter(
                status="available"
            ).count(),




        # EMPLOYEES

        "total_employees":
            Employee.objects.count(),




        # RENTALS

        "active_rentals":
            Rental.objects.filter(
                status="active"
            ).count(),




        # PROJECTS

        "active_projects":
            Project.objects.filter(
                status="active"
            ).count(),




        # MAINTENANCE

        "maintenance_due":
            MaintenanceRecord.objects.filter(
                status="pending"
            ).count(),


    }







    # ==============================
    # FINANCE
    # ==============================



    income = Income.objects.filter(

        date_received__month=current_month,

        date_received__year=current_year

    ).aggregate(

        total=Sum("amount")

    )["total"] or 0






    expenses = Expense.objects.filter(

        date_paid__month=current_month,

        date_paid__year=current_year

    ).aggregate(

        total=Sum("amount")

    )["total"] or 0







    context.update({


        "monthly_revenue":
            income,


        "monthly_expenses":
            expenses,


        "monthly_profit":
            income - expenses,


    })








    # ==============================
    # REVENUE CHART
    # ==============================



    revenue = (

        Income.objects.filter(

            date_received__year=current_year

        )

        .annotate(

            month=TruncMonth(
                "date_received"
            )

        )

        .values("month")

        .annotate(

            total=Sum("amount")

        )

        .order_by("month")

    )





    context["revenue_months"] = [

        item["month"].strftime("%b")

        for item in revenue

    ]




    context["revenue_values"] = [

        float(item["total"])

        for item in revenue

    ]





    return context







# ======================================================
# MAIN ROUTER
# ======================================================



@login_required
def dashboard(request):


    role = getattr(
        request.user,
        "role",
        ""
    ).lower()



    dashboards = {


        "owner":
            "dashboard:owner_dashboard",


        "director":
            "dashboard:director_dashboard",


        "manager":
            "dashboard:manager_dashboard",


        "secretary":
            "dashboard:secretary_dashboard",

    }



    url = dashboards.get(role)



    if url:

        return redirect(url)



    return render(
        request,
        "dashboard/no_access.html"
    )









# ======================================================
# OWNER DASHBOARD
# ======================================================


@login_required
def owner_dashboard(request):


    if request.user.role.lower() != "owner":

        return redirect("dashboard:dashboard")



    return render(

        request,

        "dashboard/owner_dashboard.html",

        dashboard_context(request)

    )









# ======================================================
# DIRECTOR DASHBOARD
# ======================================================


@login_required
def director_dashboard(request):


    if request.user.role.lower() not in [
        "director",
        "owner"
    ]:

        return redirect("dashboard:dashboard")



    return render(

        request,

        "dashboard/director_dashboard.html",

        dashboard_context(request)

    )









# ======================================================
# MANAGER DASHBOARD
# ======================================================


@login_required
def manager_dashboard(request):


    if request.user.role.lower() not in [
        "manager",
        "owner"
    ]:

        return redirect("dashboard:dashboard")



    return render(

        request,

        "dashboard/manager_dashboard.html",

        dashboard_context(request)

    )









# ======================================================
# SECRETARY DASHBOARD
# ======================================================


@login_required
def secretary_dashboard(request):


    if request.user.role.lower() not in [
        "secretary",
        "owner"
    ]:

        return redirect("dashboard:dashboard")



    return render(

        request,

        "dashboard/secretary_dashboard.html",

        dashboard_context(request)

    )