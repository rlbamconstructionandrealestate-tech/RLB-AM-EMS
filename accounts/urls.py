from django.urls import path

from .views import (
    login_view,
    logout_view,
    profile,
)


urlpatterns = [

    # Login
    path(
        "",
        login_view,
        name="login"
    ),


    # Logout
    path(
        "logout/",
        logout_view,
        name="logout"
    ),


    # User Profile
    path(
        "profile/",
        profile,
        name="profile"
    ),

]