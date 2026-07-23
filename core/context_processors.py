from django.conf import settings
from django.urls import reverse, NoReverseMatch

from .menu import SIDEBAR_MENU



# =====================================================
# SIDEBAR MENU CONTEXT PROCESSOR
# =====================================================

def sidebar_menu(request):

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



        for item in section.get("items", []):


            allowed_roles = item.get(
                "roles",
                []
            )



            # ROLE ACCESS

            has_access = (

                user.is_superuser

                or role == "admin"

                or "*" in allowed_roles

                or role in allowed_roles

            )



            if not has_access:

                continue




            menu_item = item.copy()



            # ===============================
            # URL CONVERSION
            # ===============================

            url_name = menu_item.get(
                "url",
                ""
            )


            try:

                if url_name.startswith("/"):

                    menu_item["href"] = url_name


                else:

                    menu_item["href"] = reverse(
                        url_name
                    )



            except NoReverseMatch:


                menu_item["href"] = "#"




            # ===============================
            # ACTIVE MENU
            # ===============================

            menu_item["active"] = (

                menu_item["href"] != "#"

                and request.path.startswith(
                    menu_item["href"]
                )

            )



            visible_items.append(
                menu_item
            )



        if visible_items:


            menu.append({

                "section":
                    section["section"],


                "items":
                    visible_items

            })



    return {

        "sidebar_menu":
            menu

    }




# =====================================================
# COMPANY INFORMATION
# =====================================================


def company_info(request):


    return {


        "company_name":

            getattr(
                settings,
                "COMPANY_NAME",
                "RLB-AM Construction & Real Estate Ltd"
            ),



        "system_name":

            getattr(
                settings,
                "SYSTEM_NAME",
                "RLB-AM EMS"
            ),



        "system_short_name":

            getattr(
                settings,
                "SYSTEM_SHORT_NAME",
                "EMS"
            ),



        "current_year":

            getattr(
                settings,
                "CURRENT_YEAR",
                2026
            ),

    }