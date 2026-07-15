from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

from .models import Income, Expense, Invoice
from .forms import IncomeForm, ExpenseForm, InvoiceForm



# =====================================================
# FINANCE DASHBOARD
# =====================================================

@login_required
def dashboard(request):

    income_total = Income.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0


    expense_total = Expense.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0


    context = {

        "income": income_total,

        "expenses": expense_total,

        "invoices": Invoice.objects.count(),

        "profit": income_total - expense_total,


        # Forms
        "income_form": IncomeForm(),

        "expense_form": ExpenseForm(),

        "invoice_form": InvoiceForm(),

    }


    return render(
        request,
        "finance/dashboard.html",
        context
    )





# =====================================================
# ADD INCOME
# =====================================================

@login_required
def add_income(request):

    if request.method == "POST":

        form = IncomeForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Income recorded successfully."
            )


        else:

            messages.error(
                request,
                "Please correct the income form errors."
            )


    return redirect(
        "finance:dashboard"
    )





# =====================================================
# ADD EXPENSE
# =====================================================

@login_required
def add_expense(request):

    if request.method == "POST":

        form = ExpenseForm(request.POST)


        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Expense recorded successfully."
            )


        else:

            messages.error(
                request,
                "Please correct the expense form errors."
            )


    return redirect(
        "finance:dashboard"
    )





# =====================================================
# ADD INVOICE
# =====================================================

@login_required
def add_invoice(request):

    if request.method == "POST":

        form = InvoiceForm(request.POST)


        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Invoice created successfully."
            )


        else:

            messages.error(
                request,
                "Please correct the invoice form errors."
            )


    return redirect(
        "finance:dashboard"
    )





# =====================================================
# INCOME LIST
# =====================================================

@login_required
def income_list(request):

    incomes = Income.objects.all().order_by(
        "-date_received"
    )


    return render(
        request,
        "finance/income_list.html",
        {
            "incomes": incomes
        }
    )





# =====================================================
# EXPENSE LIST
# =====================================================

@login_required
def expense_list(request):

    expenses = Expense.objects.all().order_by(
        "-date_paid"
    )


    return render(
        request,
        "finance/expense_list.html",
        {
            "expenses": expenses
        }
    )





# =====================================================
# INVOICE LIST
# =====================================================

@login_required
def invoice_list(request):

    invoices = Invoice.objects.all().order_by(
        "-issue_date"
    )


    return render(
        request,
        "finance/invoice_list.html",
        {
            "invoices": invoices
        }
    )





# =====================================================
# FINANCE REPORTS
# =====================================================

@login_required
def reports(request):

    income_total = Income.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0


    expense_total = Expense.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0



    context = {

        "income": income_total,

        "expenses": expense_total,

        "profit": income_total - expense_total,


        "income_count": Income.objects.count(),

        "expense_count": Expense.objects.count(),

        "invoice_count": Invoice.objects.count(),

    }



    return render(
        request,
        "finance/reports.html",
        context
    )