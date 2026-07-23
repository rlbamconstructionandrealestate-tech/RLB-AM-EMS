from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages


# ==========================================================
# OWNER ONLY
# ==========================================================

def owner_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != "owner":

            messages.error(
                request,
                "You do not have permission to access this page."
            )

            return redirect("dashboard:dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================================
# DIRECTOR ONLY
# ==========================================================

def director_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != "director":

            messages.error(
                request,
                "You do not have permission to access this page."
            )

            return redirect("dashboard:dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================================
# MANAGER ONLY
# ==========================================================

def manager_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != "manager":

            messages.error(
                request,
                "You do not have permission to access this page."
            )

            return redirect("dashboard:dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================================
# SECRETARY ONLY
# ==========================================================

def secretary_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != "secretary":

            messages.error(
                request,
                "You do not have permission to access this page."
            )

            return redirect("dashboard:dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================================
# OWNER + MANAGER
# ==========================================================

def owner_manager_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role not in [

            "owner",

            "manager",

        ]:

            messages.error(
                request,
                "You do not have permission to access this page."
            )

            return redirect("dashboard:dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================================
# OWNER + MANAGER + SECRETARY
# ==========================================================

def operations_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role not in [

            "owner",

            "manager",

            "secretary",

        ]:

            messages.error(
                request,
                "You do not have permission to access this page."
            )

            return redirect("dashboard:dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================================
# OWNER + MANAGER + DIRECTOR
# ==========================================================

def reports_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role not in [

            "owner",

            "manager",

            "director",

        ]:

            messages.error(
                request,
                "You do not have permission to access this page."
            )

            return redirect("dashboard:dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper