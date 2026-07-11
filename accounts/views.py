from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            if not form.cleaned_data.get("remember_me"):
                request.session.set_expiry(0)

            messages.success(
                request,
                f"Welcome back {user.username}"
            )

            return redirect("dashboard")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "authentication/login.html",
        {
            "form": form
        }
    )


@login_required
def logout_view(request):

    logout(request)

    return redirect("login")