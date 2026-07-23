from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@login_required
def dashboard(request):

    context = {

        "total_properties": 0,

        "available_properties": 0,

        "sold_properties": 0,

        "rental_income": 0,

    }

    return render(
        request,
        "real_estate/dashboard.html",
        context
    )



@login_required
def property_list(request):

    return render(
        request,
        "real_estate/property_list.html",
        {
            "properties": []
        }
    )



@login_required
def create_property(request):

    return render(
        request,
        "real_estate/create_property.html"
    )



@login_required
def property_detail(request, pk):

    return render(
        request,
        "real_estate/property_detail.html",
        {
            "property_id": pk
        }
    )



@login_required
def sales(request):

    return render(
        request,
        "real_estate/sales.html"
    )



@login_required
def rentals(request):

    return render(
        request,
        "real_estate/rentals.html"
    )