from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Rental
from .forms import RentalForm



# ==========================================
# RENTALS DASHBOARD
# ==========================================

@login_required
def dashboard(request):

    context = {

        "total_rentals":
            Rental.objects.count(),


        "active_rentals":
            Rental.objects.filter(
                status="active"
            ).count(),


        "completed_rentals":
            Rental.objects.filter(
                status="completed"
            ).count(),


        "rental_revenue":
            0,

    }


    return render(

        request,

        "rentals/dashboard.html",

        context

    )





# ==========================================
# RENTAL LIST
# ==========================================

@login_required
def rental_list(request):

    rentals = Rental.objects.all().order_by(
        "-id"
    )


    context = {

        "rentals": rentals

    }


    return render(

        request,

        "rentals/list.html",

        context

    )





# ==========================================
# CREATE RENTAL
# ==========================================

@login_required
def rental_create(request):

    if request.method == "POST":

        form = RentalForm(
            request.POST
        )


        if form.is_valid():

            rental = form.save()


            messages.success(

                request,

                "Rental created successfully."

            )


            return redirect(
                "rentals:list"
            )


    else:

        form = RentalForm()



    return render(

        request,

        "rentals/form.html",

        {
            "form": form
        }

    )





# ==========================================
# RENTAL DETAIL
# ==========================================

@login_required
def rental_detail(request, pk):

    rental = get_object_or_404(

        Rental,

        pk=pk

    )


    return render(

        request,

        "rentals/detail.html",

        {
            "rental": rental
        }

    )





# ==========================================
# UPDATE RENTAL
# ==========================================

@login_required
def rental_update(request, pk):

    rental = get_object_or_404(

        Rental,

        pk=pk

    )



    if request.method == "POST":


        form = RentalForm(

            request.POST,

            instance=rental

        )



        if form.is_valid():


            form.save()



            messages.success(

                request,

                "Rental updated successfully."

            )


            return redirect(

                "rentals:list"

            )


    else:


        form = RentalForm(

            instance=rental

        )





    return render(

        request,

        "rentals/form.html",

        {
            "form": form,
            "rental": rental
        }

    )





# ==========================================
# DELETE RENTAL
# ==========================================

@login_required
def rental_delete(request, pk):

    rental = get_object_or_404(

        Rental,

        pk=pk

    )



    if request.method == "POST":


        rental.delete()



        messages.success(

            request,

            "Rental deleted successfully."

        )



        return redirect(

            "rentals:list"

        )





    return render(

        request,

        "rentals/delete.html",

        {
            "rental": rental
        }

    )