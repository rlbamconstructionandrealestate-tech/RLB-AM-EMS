from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Avg
from django.shortcuts import render, redirect, get_object_or_404


from .models import (
    Project,
    ProjectMilestone,
    ProjectExpense,
    ProjectActivity,
)


from .forms import (
    ProjectForm,
    ProjectMilestoneForm,
    ProjectExpenseForm,
)





# =====================================================
# PROJECT DASHBOARD
# =====================================================


@login_required
def dashboard(request):


    projects = Project.objects.select_related(
        "client",
        "manager"
    )



    # =====================================================
    # PROJECT STATISTICS
    # =====================================================


    total_projects = projects.count()



    ongoing_projects = projects.filter(
        status="ongoing"
    ).count()



    completed_projects = projects.filter(
        status="completed"
    ).count()



    planning_projects = projects.filter(
        status="planning"
    ).count()



    on_hold_projects = projects.filter(
        status="on_hold"
    ).count()



    cancelled_projects = projects.filter(
        status="cancelled"
    ).count()





    # =====================================================
    # FINANCIAL STATISTICS
    # =====================================================


    total_value = projects.aggregate(

        total=Sum("contract_value")

    )["total"] or 0




    total_paid = projects.aggregate(

        total=Sum("amount_paid")

    )["total"] or 0





    total_expenses = ProjectExpense.objects.aggregate(

        total=Sum("amount")

    )["total"] or 0





    outstanding_balance = (

        total_value - total_paid

    )




    estimated_profit = (

        total_value - total_expenses

    )







    # =====================================================
    # PROGRESS
    # =====================================================


    average_progress = projects.aggregate(

        avg=Avg("progress")

    )["avg"] or 0






    # =====================================================
    # STATUS CHART DATA
    # =====================================================


    status_chart = {


        "Planning": planning_projects,


        "Ongoing": ongoing_projects,


        "Completed": completed_projects,


        "On Hold": on_hold_projects,


        "Cancelled": cancelled_projects,


    }








    # =====================================================
    # RECENT PROJECTS
    # =====================================================


    recent_projects = projects.order_by(

        "-created_at"

    )[:5]






    # =====================================================
    # RECENT EXPENSES
    # =====================================================


    recent_expenses = ProjectExpense.objects.select_related(

        "project",

        "created_by"

    ).order_by(

        "-date"

    )[:5]







    context = {



        # COUNTS

        "total_projects": total_projects,

        "ongoing_projects": ongoing_projects,

        "completed_projects": completed_projects,

        "planning_projects": planning_projects,

        "on_hold_projects": on_hold_projects,

        "cancelled_projects": cancelled_projects,





        # FINANCE

        "total_value": total_value,

        "total_paid": total_paid,

        "outstanding_balance": outstanding_balance,

        "total_expenses": total_expenses,

        "estimated_profit": estimated_profit,





        # PROGRESS

        "average_progress": round(

            average_progress

        ),





        # TABLE DATA

        "recent_projects": recent_projects,


        "recent_expenses": recent_expenses,





        # CHART DATA

        "status_chart": status_chart,



    }



    return render(

        request,

        "projects/dashboard.html",

        context

    )









# =====================================================
# PROJECT LIST
# =====================================================


@login_required
def project_list(request):


    projects = Project.objects.select_related(

        "client",

        "manager"

    ).order_by(

        "-created_at"

    )



    return render(

        request,

        "projects/project_list.html",

        {

            "projects": projects

        }

    )









# =====================================================
# CREATE PROJECT
# =====================================================


@login_required
def create_project(request):


    if request.method == "POST":


        form = ProjectForm(

            request.POST

        )



        if form.is_valid():


            project = form.save()



            ProjectActivity.objects.create(

                project=project,

                user=request.user,

                message="Project created"

            )



            messages.success(

                request,

                "Project created successfully."

            )



            return redirect(

                "projects:detail",

                pk=project.pk

            )



    else:


        form = ProjectForm()





    return render(

        request,

        "projects/create_project.html",

        {

            "form": form

        }

    )









# =====================================================
# PROJECT DETAIL
# =====================================================


@login_required
def project_detail(request, pk):


    project = get_object_or_404(

        Project.objects.select_related(

            "client",

            "manager"

        ),

        pk=pk

    )





    milestones = project.milestones.all()



    expenses = project.expenses.select_related(

        "created_by"

    )



    activities = project.activities.select_related(

        "user"

    ).all()






    total_expenses = expenses.aggregate(

        total=Sum("amount")

    )["total"] or 0






    profit = (

        project.contract_value

        -

        total_expenses

    )






    return render(

        request,

        "projects/project_detail.html",

        {

            "project": project,

            "milestones": milestones,

            "expenses": expenses,

            "activities": activities,

            "total_expenses": total_expenses,

            "profit": profit,

        }

    )









# =====================================================
# EDIT PROJECT
# =====================================================


@login_required
def edit_project(request, pk):


    project = get_object_or_404(

        Project,

        pk=pk

    )



    if request.method == "POST":


        form = ProjectForm(

            request.POST,

            instance=project

        )



        if form.is_valid():


            form.save()



            ProjectActivity.objects.create(

                project=project,

                user=request.user,

                message="Project information updated"

            )



            messages.success(

                request,

                "Project updated successfully."

            )



            return redirect(

                "projects:detail",

                pk=project.pk

            )



    else:


        form = ProjectForm(

            instance=project

        )





    return render(

        request,

        "projects/edit_project.html",

        {

            "form": form,

            "project": project,

        }

    )









# =====================================================
# DELETE PROJECT
# =====================================================


@login_required
def delete_project(request, pk):


    project = get_object_or_404(

        Project,

        pk=pk

    )



    if request.method == "POST":


        project.delete()



        messages.success(

            request,

            "Project deleted successfully."

        )



        return redirect(

            "projects:list"

        )



    return render(

        request,

        "projects/delete_project.html",

        {

            "project": project

        }

    )









# =====================================================
# ADD MILESTONE
# =====================================================


@login_required
def add_milestone(request, pk):


    project = get_object_or_404(

        Project,

        pk=pk

    )



    if request.method == "POST":


        form = ProjectMilestoneForm(

            request.POST

        )



        if form.is_valid():


            milestone = form.save(

                commit=False

            )



            milestone.project = project


            milestone.save()



            ProjectActivity.objects.create(

                project=project,

                user=request.user,

                message=f"Milestone added: {milestone.name}"

            )



            messages.success(

                request,

                "Milestone added successfully."

            )



            return redirect(

                "projects:detail",

                pk=pk

            )



    else:


        form = ProjectMilestoneForm()





    return render(

        request,

        "projects/add_milestone.html",

        {

            "form": form,

            "project": project,

        }

    )









# =====================================================
# ADD EXPENSE
# =====================================================


@login_required
def add_expense(request, pk):


    project = get_object_or_404(

        Project,

        pk=pk

    )



    if request.method == "POST":


        form = ProjectExpenseForm(

            request.POST

        )



        if form.is_valid():


            expense = form.save(

                commit=False

            )



            expense.project = project


            expense.created_by = request.user



            expense.save()





            ProjectActivity.objects.create(

                project=project,

                user=request.user,

                message=f"Expense added: {expense.description}"

            )



            messages.success(

                request,

                "Expense added successfully."

            )



            return redirect(

                "projects:detail",

                pk=pk

            )



    else:


        form = ProjectExpenseForm()





    return render(

        request,

        "projects/add_expense.html",

        {

            "form": form,

            "project": project,

        }

    )