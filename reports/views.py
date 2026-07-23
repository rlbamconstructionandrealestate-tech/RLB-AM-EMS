from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth

import csv

from projects.models import Project
from equipment.models import Equipment
from finance.models import Income, Expense


# =====================================================
# REPORT DASHBOARD
# =====================================================

@login_required
def dashboard(request):

    total_income = Income.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0

    total_expenses = Expense.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0

    context = {
        "total_projects": Project.objects.count(),
        "total_equipment": Equipment.objects.count(),
        "total_income": total_income,
        "total_expenses": total_expenses,
        "profit": total_income - total_expenses,
    }

    return render(
        request,
        "reports/dashboard.html",
        context,
    )


# =====================================================
# ANALYTICS
# =====================================================

@login_required
def analytics(request):

    projects = Project.objects.all()

    income = (
        Income.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0
    )

    expenses = (
        Expense.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0
    )

    project_status = {
        "planning": projects.filter(status="planning").count(),
        "ongoing": projects.filter(status="ongoing").count(),
        "completed": projects.filter(status="completed").count(),
        "on_hold": projects.filter(status="on_hold").count(),
        "cancelled": projects.filter(status="cancelled").count(),
    }

    monthly_income = (
        Income.objects
        .annotate(
            month=TruncMonth("date_received")
        )
        .values("month")
        .annotate(
            total=Sum("amount")
        )
        .order_by("month")
    )

    monthly_expenses = (
        Expense.objects
        .annotate(
            month=TruncMonth("date_paid")
        )
        .values("month")
        .annotate(
            total=Sum("amount")
        )
        .order_by("month")
    )

    context = {
        "project_growth": projects.count(),
        "project_status": project_status,
        "equipment_count": Equipment.objects.count(),
        "income": income,
        "expenses": expenses,
        "profit": income - expenses,
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
    }

    return render(
        request,
        "reports/analytics.html",
        context,
    )


# =====================================================
# EQUIPMENT REPORTS
# =====================================================

@login_required
def equipment_reports(request):

    equipment = Equipment.objects.all()

    equipment_status = (
        equipment
        .values("status")
        .annotate(
            total=Count("id")
        )
        .order_by("status")
    )

    fuel_cost = 0

    try:
        from fuel.models import FuelRecord

        fuel_cost = (
            FuelRecord.objects.aggregate(
                total=Sum("total_cost")
            )["total"] or 0
        )

    except Exception:
        fuel_cost = 0

    context = {
        "equipment": equipment,
        "total_equipment": equipment.count(),
        "equipment_status": equipment_status,
        "fuel_cost": fuel_cost,
        "available_equipment": equipment.filter(status="available").count(),
        "working_equipment": equipment.filter(status="working").count(),
        "maintenance_equipment": equipment.filter(status="maintenance").count(),
        "rented_equipment": equipment.filter(status="rented").count(),
    }

    return render(
        request,
        "reports/equipment_reports.html",
        context,
    )

# =====================================================
# FINANCIAL REPORTS
# =====================================================

@login_required
def financial_reports(request):

    income = (
        Income.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0
    )

    expenses = (
        Expense.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0
    )

    monthly_income = (
        Income.objects
        .annotate(
            month=TruncMonth("date_received")
        )
        .values("month")
        .annotate(
            total=Sum("amount")
        )
        .order_by("month")
    )

    monthly_expenses = (
        Expense.objects
        .annotate(
            month=TruncMonth("date_paid")
        )
        .values("month")
        .annotate(
            total=Sum("amount")
        )
        .order_by("month")
    )

    context = {
        "income": income,
        "expenses": expenses,
        "profit": income - expenses,
        "income_records": Income.objects.count(),
        "expense_records": Expense.objects.count(),
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
    }

    return render(
        request,
        "finance/reports.html",
        context,
    )


# =====================================================
# PROJECT REPORTS
# =====================================================

@login_required
def project_reports(request):

    projects = Project.objects.select_related(
        "client",
        "manager",
    )

    context = {
        "projects": projects,
        "total": projects.count(),
        "value": (
            projects.aggregate(
                total=Sum("contract_value")
            )["total"] or 0
        ),
        "completed": projects.filter(status="completed").count(),
        "ongoing": projects.filter(status="ongoing").count(),
        "planning": projects.filter(status="planning").count(),
        "on_hold": projects.filter(status="on_hold").count(),
        "cancelled": projects.filter(status="cancelled").count(),
    }

    return render(
        request,
        "reports/project_reports.html",
        context,
    )


# =====================================================
# EXPORT REPORTS
# =====================================================

@login_required
def export(request):

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="RLB_AM_Project_Report.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        "Project Code",
        "Project Name",
        "Client",
        "Status",
        "Contract Value",
        "Amount Paid",
        "Balance",
    ])

    projects = Project.objects.select_related("client")

    for project in projects:

        writer.writerow([
            project.project_code,
            project.name,
            project.client.company_name if project.client else "",
            project.get_status_display(),
            project.contract_value,
            project.amount_paid,
            project.balance,
        ])

    return response