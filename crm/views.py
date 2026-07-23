from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClientForm, ContractForm
from .models import Client, Contract



# ==========================
# CRM DASHBOARD
# ==========================

@login_required
def dashboard(request):

    total_clients = Client.objects.count()

    active_clients = Client.objects.filter(
        status="active"
    ).count()


    total_contracts = Contract.objects.count()


    active_contracts = Contract.objects.filter(
        status="active"
    ).count()


    total_revenue = (
        Contract.objects
        .filter(status="active")
        .aggregate(total=Sum("total_value"))
        ["total"]
        or 0
    )


    recent_clients = Client.objects.order_by(
        "-created_at"
    )[:5]


    recent_contracts = Contract.objects.select_related(
        "client"
    ).order_by(
        "-created_at"
    )[:5]



    context = {

        "total_clients": total_clients,

        "active_clients": active_clients,

        "total_contracts": total_contracts,

        "active_contracts": active_contracts,

        "total_revenue": total_revenue,

        "recent_clients": recent_clients,

        "recent_contracts": recent_contracts,

    }



    return render(
        request,
        "crm/dashboard.html",
        context
    )





# ==========================
# CLIENT LIST
# ==========================

@login_required
def client_list(request):

    clients = Client.objects.annotate(
        contract_count=Count("contracts")
    ).order_by(
        "company_name"
    )


    return render(
        request,
        "crm/client_list.html",
        {
            "clients": clients
        }
    )





# ==========================
# CREATE CLIENT
# ==========================

@login_required
def create_client(request):

    if request.method == "POST":

        form = ClientForm(
            request.POST
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Client created successfully."
            )


            return redirect(
                "crm:clients"
            )


    else:

        form = ClientForm()



    return render(
        request,
        "crm/create_client.html",
        {
            "form": form
        }
    )





# ==========================
# CLIENT DETAIL
# ==========================

@login_required
def client_detail(request, pk):

    client = get_object_or_404(
        Client,
        pk=pk
    )


    contracts = client.contracts.all().order_by(
        "-created_at"
    )


    total_value = (
        contracts.aggregate(
            total=Sum("total_value")
        )["total"]
        or 0
    )


    context = {

        "client": client,

        "contracts": contracts,

        "total_value": total_value,

    }



    return render(
        request,
        "crm/client_detail.html",
        context
    )





# ==========================
# EDIT CLIENT
# ==========================

@login_required
def edit_client(request, pk):

    client = get_object_or_404(
        Client,
        pk=pk
    )


    if request.method == "POST":

        form = ClientForm(
            request.POST,
            instance=client
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Client updated successfully."
            )


            return redirect(
                "crm:client_detail",
                pk=client.pk
            )


    else:

        form = ClientForm(
            instance=client
        )



    return render(
        request,
        "crm/edit_client.html",
        {
            "form": form,
            "client": client
        }
    )





# ==========================
# DELETE CLIENT
# ==========================

@login_required
def delete_client(request, pk):

    client = get_object_or_404(
        Client,
        pk=pk
    )


    if request.method == "POST":

        client.delete()


        messages.success(
            request,
            "Client deleted successfully."
        )


        return redirect(
            "crm:clients"
        )



    return render(
        request,
        "crm/delete_client.html",
        {
            "client": client
        }
    )





# ==========================
# CONTRACT LIST
# ==========================

@login_required
def contracts(request):

    contracts = Contract.objects.select_related(
        "client"
    ).order_by(
        "-created_at"
    )



    return render(
        request,
        "crm/contracts.html",
        {
            "contracts": contracts
        }
    )





# ==========================
# CREATE CONTRACT
# ==========================

@login_required
def create_contract(request):

    if request.method == "POST":

        form = ContractForm(
            request.POST
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Contract created successfully."
            )


            return redirect(
                "crm:contracts"
            )


    else:

        form = ContractForm()



    return render(
        request,
        "crm/create_contract.html",
        {
            "form": form
        }
    )





# ==========================
# EDIT CONTRACT
# ==========================

@login_required
def edit_contract(request, pk):

    contract = get_object_or_404(
        Contract,
        pk=pk
    )


    if request.method == "POST":

        form = ContractForm(
            request.POST,
            instance=contract
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Contract updated successfully."
            )


            return redirect(
                "crm:contracts"
            )



    else:

        form = ContractForm(
            instance=contract
        )



    return render(
        request,
        "crm/edit_contract.html",
        {
            "form": form,
            "contract": contract
        }
    )





# ==========================
# DELETE CONTRACT
# ==========================

@login_required
def delete_contract(request, pk):

    contract = get_object_or_404(
        Contract,
        pk=pk
    )


    if request.method == "POST":

        contract.delete()


        messages.success(
            request,
            "Contract deleted successfully."
        )


        return redirect(
            "crm:contracts"
        )



    return render(
        request,
        "crm/delete_contract.html",
        {
            "contract": contract
        }
    )