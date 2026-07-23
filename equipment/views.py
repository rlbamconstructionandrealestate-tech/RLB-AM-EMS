from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from django.db.models import (
    Count,
    Sum,
    Q
)


from .models import Equipment
from .forms import EquipmentForm




# ==========================================
# DASHBOARD
# ==========================================


def equipment_dashboard(request):


    equipment = Equipment.objects.all()



    context = {


        "total_equipment":
            equipment.count(),



        "available_count":
            equipment.filter(
                status="available"
            ).count(),



        "working_count":
            equipment.filter(
                status="working"
            ).count(),



        "maintenance_count":
            equipment.filter(
                status="maintenance"
            ).count(),



        "total_purchase_value":

            equipment.aggregate(
                total=Sum(
                    "purchase_price"
                )
            )["total"] or 0,



        "current_asset_value":

            equipment.aggregate(
                total=Sum(
                    "current_value"
                )
            )["total"] or 0,



        "equipment_status":

            list(

                equipment.values(
                    "status"
                )

                .annotate(
                    total=Count("id")
                )

            ),



        "equipment_categories":

            list(

                equipment.values(
                    "category"
                )

                .annotate(
                    total=Count("id")
                )

                .order_by("-total")

            ),



        "recent_equipment":

            equipment.order_by(
                "-created_at"
            )[:8]

    }




    return render(
        request,
        "equipment/dashboard.html",
        context
    )







# ==========================================
# LIST
# ==========================================


def equipment_list(request):


    equipment = Equipment.objects.all()



    search = request.GET.get(
        "search"
    )


    status = request.GET.get(
        "status"
    )



    if search:


        equipment = equipment.filter(

            Q(name__icontains=search)
            |
            Q(asset_number__icontains=search)
            |
            Q(category__icontains=search)
            |
            Q(manufacturer__icontains=search)
            |
            Q(model__icontains=search)

        )



    if status:


        equipment = equipment.filter(
            status=status
        )




    return render(

        request,

        "equipment/equipment_list.html",

        {

            "equipment":
                equipment.order_by(
                    "-created_at"
                )

        }

    )







# ==========================================
# CREATE
# ==========================================


def create_equipment(request):


    if request.method == "POST":


        form = EquipmentForm(
            request.POST,
            request.FILES
        )



        if form.is_valid():


            equipment = form.save()



            messages.success(
                request,
                "Equipment added successfully."
            )



            return redirect(
                "equipment:detail",
                equipment.pk
            )



    else:


        form = EquipmentForm()




    return render(

        request,

        "equipment/create.html",

        {
            "form":form
        }

    )







# ==========================================
# DETAIL
# ==========================================


def equipment_detail(request, pk):


    equipment = get_object_or_404(
        Equipment,
        pk=pk
    )



    return render(

        request,

        "equipment/detail.html",

        {
            "equipment":equipment
        }

    )







# ==========================================
# UPDATE
# ==========================================


def update_equipment(request, pk):


    equipment = get_object_or_404(
        Equipment,
        pk=pk
    )



    if request.method == "POST":


        form = EquipmentForm(

            request.POST,

            request.FILES,

            instance=equipment

        )



        if form.is_valid():


            form.save()



            messages.success(
                request,
                "Equipment updated successfully."
            )



            return redirect(
                "equipment:detail",
                equipment.pk
            )



    else:


        form = EquipmentForm(
            instance=equipment
        )




    return render(

        request,

        "equipment/update.html",

        {

            "form":form,

            "equipment":equipment

        }

    )







# ==========================================
# DELETE
# ==========================================


def delete_equipment(request, pk):


    equipment = get_object_or_404(
        Equipment,
        pk=pk
    )



    if request.method == "POST":


        equipment.delete()



        messages.success(
            request,
            "Equipment deleted successfully."
        )



        return redirect(
            "equipment:list"
        )




    return render(

        request,

        "equipment/delete.html",

        {
            "equipment":equipment
        }

    )