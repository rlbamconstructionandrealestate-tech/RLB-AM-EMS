from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):

    context = {
        "equipment_count": 0,
        "active_rentals": 0,
        "employee_count": 0,
        "monthly_revenue": 0,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )