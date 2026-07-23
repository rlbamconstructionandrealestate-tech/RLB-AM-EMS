from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    CompanyProfile,
    SystemPreference,
    NotificationSetting,
)

from .forms import (
    CompanyProfileForm,
    SystemPreferenceForm,
    NotificationSettingForm,
)





# =====================================================
# ADMIN / DIRECTOR PERMISSION
# =====================================================


def admin_access(user):

    role = getattr(user, "role", "")

    role = role.lower() if role else ""


    return (

        user.is_superuser

        or role in [
            "admin",
            "director",
        ]

    )







# =====================================================
# SETTINGS DASHBOARD
# =====================================================


@login_required
@user_passes_test(admin_access)
def dashboard(request):


    company = CompanyProfile.objects.first()


    system = SystemPreference.objects.first()



    context = {


        "company": company,


        "system": system,


    }



    return render(

        request,

        "settings_app/dashboard.html",

        context

    )









# =====================================================
# COMPANY PROFILE
# =====================================================


@login_required
@user_passes_test(admin_access)
def company_profile(request):


    company = CompanyProfile.objects.first()



    if not company:


        company = CompanyProfile.objects.create()





    if request.method == "POST":


        form = CompanyProfileForm(

            request.POST,

            request.FILES,

            instance=company

        )



        if form.is_valid():


            form.save()



            messages.success(

                request,

                "Company profile updated successfully."

            )



            return redirect(

                "settings_app:company"

            )




    else:


        form = CompanyProfileForm(

            instance=company

        )






    return render(

        request,

        "settings_app/company.html",

        {

            "form": form,

            "company": company,

        }

    )









# =====================================================
# SYSTEM PREFERENCES
# =====================================================


@login_required
@user_passes_test(admin_access)
def system_preferences(request):


    system = SystemPreference.objects.first()



    if not system:


        system = SystemPreference.objects.create()





    if request.method == "POST":


        form = SystemPreferenceForm(

            request.POST,

            instance=system

        )



        if form.is_valid():


            form.save()



            messages.success(

                request,

                "System preferences updated."

            )



            return redirect(

                "settings_app:system"

            )





    else:


        form = SystemPreferenceForm(

            instance=system

        )







    return render(

        request,

        "settings_app/system.html",

        {

            "form": form,

            "system": system,

        }

    )









# =====================================================
# NOTIFICATION SETTINGS
# =====================================================


@login_required
def notification_settings(request):


    notification, created = NotificationSetting.objects.get_or_create(

        user=request.user

    )





    if request.method == "POST":


        form = NotificationSettingForm(

            request.POST,

            instance=notification

        )



        if form.is_valid():


            form.save()



            messages.success(

                request,

                "Notification settings saved."

            )



            return redirect(

                "settings_app:notifications"

            )





    else:


        form = NotificationSettingForm(

            instance=notification

        )






    return render(

        request,

        "settings_app/notifications.html",

        {

            "form": form,

        }

    )