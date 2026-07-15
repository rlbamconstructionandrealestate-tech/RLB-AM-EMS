from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Q, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EquipmentForm
from .models import Equipment, EquipmentCategory


@login_required
def equipment_dashboard(request):
    equipment = Equipment.objects.select_related("category")

    context = {
        "total_equipment": equipment.count(),
        "available_count": equipment.filter(status="Available").count(),
        "working_count": equipment.filter(status="Working").count(),
        "rented_count": equipment.filter(status="Rented").count(),
        "maintenance_count": equipment.filter(status="Maintenance").count(),
        "out_service_count": equipment.filter(
            status="Out of Service"
        ).count(),
        "total_purchase_value": equipment.aggregate(
            total=Sum("purchase_price")
        )["total"] or 0,
        "equipment_by_category": EquipmentCategory.objects.annotate(
            total=Count("equipments")
        ),
        "recent_equipment": equipment.order_by("-created_at")[:10],
    }

    return render(
        request,
        "equipment/dashboard.html",
        context,
    )


@login_required
def equipment_list(request):

    queryset = Equipment.objects.select_related(
        "category"
    ).order_by("name")

    search = request.GET.get("search")

    if search:
        queryset = queryset.filter(
            Q(name__icontains=search)
            | Q(asset_number__icontains=search)
            | Q(registration_number__icontains=search)
            | Q(serial_number__icontains=search)
            | Q(manufacturer__icontains=search)
            | Q(model__icontains=search)
            | Q(current_location__icontains=search)
        )

    status = request.GET.get("status")

    if status:
        queryset = queryset.filter(status=status)

    category = request.GET.get("category")

    if category:
        queryset = queryset.filter(category_id=category)

    manufacturer = request.GET.get("manufacturer")

    if manufacturer:
        queryset = queryset.filter(
            manufacturer__icontains=manufacturer
        )

    active = request.GET.get("active")

    if active == "yes":
        queryset = queryset.filter(is_active=True)

    elif active == "no":
        queryset = queryset.filter(is_active=False)

    ordering = request.GET.get("ordering")

    if ordering:

        allowed = [
            "name",
            "-name",
            "purchase_price",
            "-purchase_price",
            "daily_rate",
            "-daily_rate",
            "manufacture_year",
            "-manufacture_year",
            "created_at",
            "-created_at",
        ]

        if ordering in allowed:
            queryset = queryset.order_by(ordering)

    paginator = Paginator(queryset, 12)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {

        "page_obj": page_obj,

        "equipment_list": page_obj,

        "categories": EquipmentCategory.objects.all(),

        "status_choices": Equipment.STATUS_CHOICES,

        "search": search,

        "selected_status": status,

        "selected_category": category,

        "selected_manufacturer": manufacturer,

        "selected_active": active,

        "selected_ordering": ordering,

    }

    return render(
        request,
        "equipment/equipment_list.html",
        context,
    )

@login_required
def equipment_create(request):
    """
    Create a new equipment record.
    """

    if request.method == "POST":

        form = EquipmentForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            equipment = form.save()

            messages.success(
                request,
                f"{equipment.name} was added successfully.",
            )

            return redirect(
                "equipment:detail",
                pk=equipment.pk,
            )

        messages.error(
            request,
            "Please correct the errors below.",
        )

    else:

        form = EquipmentForm()

    return render(
        request,
        "equipment/equipment_form.html",
        {
            "form": form,
            "title": "Add Equipment",
            "button_text": "Save Equipment",
        },
    )


@login_required
def equipment_update(request, pk):
    """
    Edit an existing equipment record.
    """

    equipment = get_object_or_404(
        Equipment,
        pk=pk,
    )

    if request.method == "POST":

        form = EquipmentForm(
            request.POST,
            request.FILES,
            instance=equipment,
        )

        if form.is_valid():

            equipment = form.save()

            messages.success(
                request,
                "Equipment updated successfully.",
            )

            return redirect(
                "equipment:detail",
                pk=equipment.pk,
            )

        messages.error(
            request,
            "Please correct the errors below.",
        )

    else:

        form = EquipmentForm(
            instance=equipment,
        )

    return render(
        request,
        "equipment/equipment_form.html",
        {
            "form": form,
            "equipment": equipment,
            "title": "Edit Equipment",
            "button_text": "Update Equipment",
        },
    )


@login_required
def equipment_detail(request, pk):
    """
    Display equipment details.
    """

    equipment = get_object_or_404(
        Equipment.objects.select_related("category"),
        pk=pk,
    )

    context = {
        "equipment": equipment,
    }

    return render(
        request,
        "equipment/equipment_detail.html",
        context,
    )


@login_required
def equipment_delete(request, pk):
    """
    Delete equipment.
    """

    equipment = get_object_or_404(
        Equipment,
        pk=pk,
    )

    if request.method == "POST":

        equipment_name = equipment.name

        equipment.delete()

        messages.success(
            request,
            f'"{equipment_name}" was deleted successfully.',
        )

        return redirect(
            "equipment:list",
        )

    return render(
        request,
        "equipment/equipment_confirm_delete.html",
        {
            "equipment": equipment,
        },
    )