from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from django.db.models import Sum, Count

from .models import MaintenanceRecord

from .forms import MaintenanceRecordForm





# ==========================================
# MAINTENANCE DASHBOARD
# ==========================================

def maintenance_dashboard(request):


    records = MaintenanceRecord.objects.select_related(
        "equipment"
    ).order_by(
        "-service_date"
    )



    context = {


        "total_records":
            records.count(),



        "completed_count":
            records.filter(
                status="completed"
            ).count(),



        "pending_count":
            records.filter(
                status="pending"
            ).count(),



        "scheduled_count":
            records.filter(
                status="scheduled"
            ).count(),



        "total_cost":
            records.aggregate(
                total=Sum("cost")
            )["total"] or 0,



        "recent_records":
            records[:10],

    }



    return render(

        request,

        "maintenance/dashboard.html",

        context

    )








# ==========================================
# MAINTENANCE LIST
# ==========================================

def maintenance_list(request):


    records = MaintenanceRecord.objects.select_related(
        "equipment"
    ).all()



    search = request.GET.get(
        "search"
    )


    if search:


        records = records.filter(

            equipment__name__icontains=search

        )



    context = {


        "records":
            records,


    }



    return render(

        request,

        "maintenance/list.html",

        context

    )









# ==========================================
# CREATE
# ==========================================

def maintenance_create(request):


    if request.method == "POST":


        form = MaintenanceRecordForm(
            request.POST
        )


        if form.is_valid():

            form.save()


            messages.success(

                request,

                "Maintenance record created successfully."

            )


            return redirect(
                "maintenance:list"
            )


    else:


        form = MaintenanceRecordForm()



    return render(

        request,

        "maintenance/form.html",

        {

            "form": form,

        }

    )









# ==========================================
# DETAIL
# ==========================================

def maintenance_detail(request, pk):


    record = get_object_or_404(

        MaintenanceRecord,

        pk=pk

    )



    return render(

        request,

        "maintenance/detail.html",

        {

            "record": record

        }

    )









# ==========================================
# UPDATE
# ==========================================

def maintenance_update(request, pk):


    record = get_object_or_404(

        MaintenanceRecord,

        pk=pk

    )



    if request.method == "POST":


        form = MaintenanceRecordForm(

            request.POST,

            instance=record

        )



        if form.is_valid():


            form.save()


            messages.success(

                request,

                "Maintenance updated successfully."

            )


            return redirect(

                "maintenance:list"

            )



    else:


        form = MaintenanceRecordForm(

            instance=record

        )




    return render(

        request,

        "maintenance/form.html",

        {

            "form": form,

            "record": record

        }

    )









# ==========================================
# DELETE
# ==========================================

def maintenance_delete(request, pk):


    record = get_object_or_404(

        MaintenanceRecord,

        pk=pk

    )



    if request.method == "POST":


        record.delete()


        messages.success(

            request,

            "Maintenance record deleted."

        )


        return redirect(

            "maintenance:list"

        )



    return render(

        request,

        "maintenance/delete.html",

        {

            "record": record

        }

    )