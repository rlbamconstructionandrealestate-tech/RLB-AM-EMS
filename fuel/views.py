from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FuelRecordForm
from .models import FuelRecord



# ======================================================
# FUEL DASHBOARD
# ======================================================

@login_required
def dashboard(request):

    fuel_records = FuelRecord.objects.select_related(
        "machine"
    ).order_by(
        "-date",
        "-id"
    )[:10]


    total_records = FuelRecord.objects.count()


    total_litres = FuelRecord.objects.aggregate(
        total=Sum("litres")
    )["total"] or 0



    total_cost = FuelRecord.objects.aggregate(
        total=Sum("total_cost")
    )["total"] or 0



    average_price = FuelRecord.objects.aggregate(
        avg=Avg("price_per_litre")
    )["avg"] or 0



    context = {

        "fuel_records": fuel_records,

        "total_records": total_records,

        "total_litres": total_litres,

        "total_cost": total_cost,

        "average_price": average_price,

    }


    return render(
        request,
        "fuel/dashboard.html",
        context
    )





# ======================================================
# FUEL RECORD LIST
# ======================================================

@login_required
def fuel_list(request):

    records = FuelRecord.objects.select_related(
        "machine"
    ).order_by(
        "-date",
        "-id"
    )


    return render(
        request,
        "fuel/fuel_list.html",
        {
            "records": records,
        }
    )





# ======================================================
# ADD FUEL RECORD
# ======================================================

@login_required
def fuel_create(request):

    if request.method == "POST":

        form = FuelRecordForm(request.POST)

        if form.is_valid():

            fuel = form.save(commit=False)

            fuel.created_by = request.user if hasattr(
                fuel,
                "created_by"
            ) else None

            fuel.save()


            messages.success(
                request,
                "Fuel record created successfully."
            )


            return redirect(
                "fuel:list"
            )


    else:

        form = FuelRecordForm()



    return render(
        request,
        "fuel/fuel_form.html",
        {
            "form": form,
            "title": "Add Fuel Record",
        }
    )





# ======================================================
# FUEL DETAILS
# ======================================================

@login_required
def fuel_detail(request, pk):

    record = get_object_or_404(
        FuelRecord,
        pk=pk
    )


    return render(
        request,
        "fuel/fuel_detail.html",
        {
            "record": record,
        }
    )





# ======================================================
# EDIT FUEL RECORD
# ======================================================

@login_required
def fuel_update(request, pk):

    record = get_object_or_404(
        FuelRecord,
        pk=pk
    )


    if request.method == "POST":

        form = FuelRecordForm(
            request.POST,
            instance=record
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Fuel record updated successfully."
            )


            return redirect(
                "fuel:detail",
                pk=record.pk
            )


    else:

        form = FuelRecordForm(
            instance=record
        )



    return render(
        request,
        "fuel/fuel_form.html",
        {
            "form": form,
            "title": "Edit Fuel Record",
        }
    )





# ======================================================
# DELETE FUEL RECORD
# ======================================================

@login_required
def fuel_delete(request, pk):

    record = get_object_or_404(
        FuelRecord,
        pk=pk
    )


    if request.method == "POST":

        record.delete()


        messages.success(
            request,
            "Fuel record deleted successfully."
        )


        return redirect(
            "fuel:list"
        )



    return render(
        request,
        "fuel/fuel_confirm_delete.html",
        {
            "record": record,
        }
    )