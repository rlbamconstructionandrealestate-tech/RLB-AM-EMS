# core/context_processors.py

from django.conf import settings
from django.urls import reverse, NoReverseMatch

from .menu import SIDEBAR_MENU



# =====================================================
# SIDEBAR MENU CONTEXT PROCESSOR
# =====================================================


def sidebar_menu(request):
    """
    Builds sidebar menu dynamically based on user role.

    Adds:
        href   -> resolved URL
        active -> active sidebar state
    """


    if not request.user.is_authenticated:

        return {
            "sidebar_menu": []
        }



    user = request.user


    role = getattr(
        user,
        "role",
        ""
    )


    role = role.lower() if role else ""



    menu = []




    for section in SIDEBAR_MENU:


        visible_items = []



        for item in section["items"]:



            roles = item.get(
                "roles",
                []
            )




            # =============================================
            # ROLE PERMISSION CHECK
            # =============================================


            allowed = (

                user.is_superuser

                or "*" in roles

                or role == "admin"

                or role in roles

            )



            if not allowed:

                continue






            menu_item = item.copy()





            # =============================================
            # URL RESOLUTION
            # =============================================


            try:


                if menu_item["url"].startswith("/"):


                    menu_item["href"] = menu_item["url"]



                else:


                    menu_item["href"] = reverse(
                        menu_item["url"]
                    )



            except NoReverseMatch:


                menu_item["href"] = "#"








            # =============================================
            # ACTIVE STATE
            # =============================================


            menu_item["active"] = (

                request.path == menu_item["href"]

                or (

                    menu_item["href"] != "#"

                    and request.path.startswith(
                        menu_item["href"]
                    )

                )

            )





            visible_items.append(
                menu_item
            )






        if visible_items:


            menu.append(

                {

                    "section": section["section"],

                    "items": visible_items,

                }

            )





    return {

        "sidebar_menu": menu

    }









# =====================================================
# COMPANY INFORMATION
# =====================================================


def company_info(request):


    return {


        "company_name": getattr(

            settings,

            "COMPANY_NAME",

            "RLB-AM Construction & Real Estate Ltd"

        ),



        "system_name": getattr(

            settings,

            "SYSTEM_NAME",

            "RLB-AM EMS"

        ),



        "system_short_name": getattr(

            settings,

            "SYSTEM_SHORT_NAME",

            "EMS"

        ),



        "current_year": 2026,


    }