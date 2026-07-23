from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import (
    LoginForm,
    UserProfileForm,
    CustomPasswordChangeForm,
)



# ======================================================
# LOGIN
# ======================================================

def login_view(request):

    if request.user.is_authenticated:
        return get_role_redirect(request.user)


    if request.method == "POST":

        form = LoginForm(
            request,
            data=request.POST
        )


        if form.is_valid():

            user = form.get_user()


            login(
                request,
                user
            )


            if not form.cleaned_data.get(
                "remember_me"
            ):

                request.session.set_expiry(0)



            messages.success(
                request,
                f"Welcome back, {user.get_full_name() or user.username}!"
            )


            return get_role_redirect(user)



        messages.error(
            request,
            "Invalid username or password."
        )


    else:

        form = LoginForm(request)



    return render(
        request,
        "authentication/login.html",
        {
            "form":form
        }
    )





# ======================================================
# ROLE REDIRECT
# ======================================================

def get_role_redirect(user):

    dashboards = {

        "owner":
        "dashboard:owner_dashboard",

        "director":
        "dashboard:director_dashboard",

        "manager":
        "dashboard:manager_dashboard",

        "secretary":
        "dashboard:secretary_dashboard",

    }


    return redirect(
        dashboards.get(
            user.role,
            "dashboard:dashboard"
        )
    )





# ======================================================
# LOGOUT
# ======================================================

@login_required
def logout_view(request):

    logout(request)


    messages.success(
        request,
        "Logged out successfully."
    )


    return redirect(
        "accounts:login"
    )





# ======================================================
# PROFILE
# ======================================================

@login_required
def profile(request):

    return render(
        request,
        "accounts/profile.html",
        {
            "user_profile":request.user
        }
    )





# ======================================================
# EDIT PROFILE
# ======================================================

@login_required
def edit_profile(request):

    if request.method == "POST":

        form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Profile updated successfully."
            )


            return redirect(
                "accounts:profile"
            )


    else:

        form = UserProfileForm(
            instance=request.user
        )



    return render(
        request,
        "accounts/edit_profile.html",
        {
            "form":form
        }
    )





# ======================================================
# CHANGE PASSWORD
# ======================================================

@login_required
def change_password(request):

    if request.method == "POST":

        form = CustomPasswordChangeForm(
            request.user,
            request.POST
        )


        if form.is_valid():

            form.save()


            messages.success(
                request,
                "Password changed successfully."
            )


            return redirect(
                "accounts:profile"
            )


    else:

        form = CustomPasswordChangeForm(
            request.user
        )


    return render(
        request,
        "accounts/change_password.html",
        {
            "form":form
        }
    )





# ======================================================
# USER MANAGEMENT
# ONLY MANAGING DIRECTOR
# ======================================================

@login_required
def user_list(request):

    if not request.user.can_manage_users():

        messages.warning(
            request,
            "You don't have permission to manage users."
        )

        return redirect(
            "accounts:profile"
        )



    from .models import User


    users = User.objects.all().order_by(
        "role",
        "first_name"
    )


    return render(
        request,
        "accounts/users.html",
        {
            "users":users,
            "title":"User Management"
        }
    )

# ======================================================
# REGISTER
# ======================================================

def register_view(request):

    if request.user.is_authenticated:
        return get_role_redirect(request.user)


    if request.method == "POST":

        form = RegisterForm(request.POST)


        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )


            messages.success(
                request,
                f"Welcome {user.username}, your account was created successfully."
            )


            return get_role_redirect(user)


        else:

            messages.error(
                request,
                "Please correct the errors below."
            )


    else:

        form = RegisterForm()


    return render(
        request,
        "authentication/register.html",
        {
            "form": form
        }
    )