from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import (
    LoginForm,
    RegisterForm,
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


            # Remember me
            if not form.cleaned_data.get("remember_me"):

                request.session.set_expiry(0)


            messages.success(
                request,
                f"Welcome back, {user.username}!"
            )


            return get_role_redirect(user)


        else:

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
            "form": form
        }
    )



# ======================================================
# REGISTER
# ======================================================

def register_view(request):

    if request.user.is_authenticated:
        return get_role_redirect(request.user)


    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )


        if form.is_valid():

            user = form.save()


            login(
                request,
                user
            )


            messages.success(
                request,
                f"Account created successfully! Welcome, {user.username}."
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



# ======================================================
# ROLE REDIRECT
# ======================================================

def get_role_redirect(user):

    role = getattr(
        user,
        "role",
        None
    )


    # All authorized EMS users
    # enter the main dashboard

    allowed_roles = [

        "manager",
        "secretary",
        "director",
        "engineer",
        "qs",
        "equipment",
        "fuel",

    ]


    if role in allowed_roles:

        return redirect(
            "dashboard:dashboard"
        )


    # Default fallback

    return redirect(
        "dashboard:dashboard"
    )



# ======================================================
# LOGOUT
# ======================================================

@login_required
def logout_view(request):

    logout(
        request
    )


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
            "user_profile": request.user
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
                "Your profile has been updated successfully!"
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
            "form": form
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
                "Your password has been changed successfully!"
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
            "form": form
        }
    )