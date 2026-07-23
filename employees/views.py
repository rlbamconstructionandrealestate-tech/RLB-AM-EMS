from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Employee
from .forms import EmployeeForm



# =====================================================
# EMPLOYEE DASHBOARD
# =====================================================

@login_required
def dashboard(request):


    total_employees = Employee.objects.count()



    active_employees = Employee.objects.filter(
        status="active"
    ).count()



    inactive_employees = Employee.objects.filter(
        status="inactive"
    ).count()



    leave_employees = Employee.objects.filter(
        status="leave"
    ).count()



    terminated_employees = Employee.objects.filter(
        status="terminated"
    ).count()



    recent_employees = Employee.objects.all().order_by(
        "-created_at"
    )[:5]



    context = {


        "total_employees":
            total_employees,


        "active_employees":
            active_employees,


        "inactive_employees":
            inactive_employees,


        "leave_employees":
            leave_employees,


        "terminated_employees":
            terminated_employees,


        "recent_employees":
            recent_employees,


    }



    return render(

        request,

        "employees/dashboard.html",

        context

    )






# =====================================================
# EMPLOYEE LIST
# =====================================================

@login_required
def employee_list(request):


    employees = Employee.objects.all().order_by(
        "first_name"
    )



    context = {

        "employees": employees

    }



    return render(

        request,

        "employees/list.html",

        context

    )






# =====================================================
# ADD EMPLOYEE
# =====================================================

@login_required
def employee_create(request):


    if request.method == "POST":


        form = EmployeeForm(

            request.POST,

            request.FILES

        )



        if form.is_valid():


            employee = form.save()



            messages.success(

                request,

                f"{employee.full_name} added successfully"

            )



            return redirect(

                "employees:list"

            )



    else:


        form = EmployeeForm()




    return render(

        request,

        "employees/form.html",

        {

            "form": form

        }

    )







# =====================================================
# UPDATE EMPLOYEE
# =====================================================

@login_required
def employee_update(request, pk):


    employee = get_object_or_404(

        Employee,

        pk=pk

    )



    if request.method == "POST":


        form = EmployeeForm(

            request.POST,

            request.FILES,

            instance=employee

        )



        if form.is_valid():


            form.save()



            messages.success(

                request,

                "Employee updated successfully"

            )



            return redirect(

                "employees:list"

            )



    else:


        form = EmployeeForm(

            instance=employee

        )





    return render(

        request,

        "employees/form.html",

        {

            "form": form,

            "employee": employee

        }

    )







# =====================================================
# DELETE EMPLOYEE
# =====================================================

@login_required
def employee_delete(request, pk):


    employee = get_object_or_404(

        Employee,

        pk=pk

    )



    if request.method == "POST":


        name = employee.full_name



        employee.delete()



        messages.success(

            request,

            f"{name} deleted successfully"

        )



        return redirect(

            "employees:list"

        )





    return render(

        request,

        "employees/delete.html",

        {

            "employee": employee

        }

    )

# =====================================================
# ATTENDANCE
# =====================================================

@login_required
def attendance(request):

    employees = Employee.objects.all()


    context = {

        "employees": employees

    }


    return render(

        request,

        "employees/attendance.html",

        context

    )





# =====================================================
# PAYROLL
# =====================================================

@login_required
def payroll(request):

    employees = Employee.objects.all()


    context = {

        "employees": employees

    }


    return render(

        request,

        "employees/payroll.html",

        context

    )