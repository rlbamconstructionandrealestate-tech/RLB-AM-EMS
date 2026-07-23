# ==========================================================
# RLB-AM EMS V6.1
# ENTERPRISE SIDEBAR MENU CONFIGURATION
# ==========================================================


SIDEBAR_MENU = [


    # ======================================================
    # MAIN
    # ======================================================

    {
        "section": "MAIN",

        "items": [

            {
                "name": "Dashboard",
                "icon": "bi-speedometer2",
                "url": "dashboard:dashboard",

                "roles": [
                    "owner",
                    "director",
                    "manager",
                    "secretary",
                ],
            },

        ],
    },



    # ======================================================
    # OPERATIONS
    # ======================================================

    {
        "section": "OPERATIONS",

        "items": [

            {
                "name": "Equipment",
                "icon": "bi-truck",
                "url": "equipment:list",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Fuel Management",
                "icon": "bi-fuel-pump-fill",
                "url": "fuel:dashboard",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Maintenance",
                "icon": "bi-tools",
                "url": "maintenance:dashboard",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Rentals",
                "icon": "bi-calendar-check",
                "url": "rentals:dashboard",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Project Dashboard",
                "icon": "bi-speedometer",
                "url": "projects:dashboard",

                "roles": [
                    "owner",
                    "director",
                    "manager",
                ],
            },


            {
                "name": "Projects",
                "icon": "bi-building",
                "url": "projects:list",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },

        ],
    },



    # ======================================================
    # CRM
    # ======================================================

    {
        "section": "CRM",

        "items": [

            {
                "name": "CRM Dashboard",
                "icon": "bi-people",
                "url": "crm:dashboard",

                "roles": [
                    "owner",
                    "director",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Clients",
                "icon": "bi-person-lines-fill",
                "url": "crm:clients",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Contracts",
                "icon": "bi-file-earmark-text",
                "url": "crm:contracts",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },

        ],
    },



    # ======================================================
    # FINANCE
    # ======================================================

    {

        "section": "FINANCE",

        "items": [


            {
                "name": "Finance Dashboard",
                "icon": "bi-bank",
                "url": "finance:dashboard",

                "roles": [
                    "owner",
                    "director",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Income",
                "icon": "bi-cash-stack",
                "url": "finance:add_income",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Expenses",
                "icon": "bi-wallet2",
                "url": "finance:add_expense",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Invoices",
                "icon": "bi-receipt",
                "url": "finance:add_invoice",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },

        ],
    },



    # ======================================================
    # HUMAN RESOURCES
    # ======================================================

    {

        "section": "HUMAN RESOURCES",

        "items": [

            {
                "name": "Employees",
                "icon": "bi-person-badge",
                "url": "employees:list",

                "roles": [
                    "owner",
                    "manager",
                ],
            },


            {
                "name": "Attendance",
                "icon": "bi-calendar2-check",
                "url": "employees:attendance",

                "roles": [
                    "owner",
                    "manager",
                ],
            },


            {
                "name": "Payroll",
                "icon": "bi-wallet",
                "url": "employees:payroll",

                "roles": [
                    "owner",
                    "manager",
                ],
            },

        ],
    },



    # ======================================================
    # REPORTS
    # ======================================================

    {

        "section": "REPORTS",

        "items": [

            {
                "name": "Reports",
                "icon": "bi-graph-up",
                "url": "reports:dashboard",

                "roles": [
                    "owner",
                    "director",
                    "manager",
                ],
            },


            {
                "name": "Analytics",
                "icon": "bi-pie-chart",
                "url": "reports:analytics",

                "roles": [
                    "owner",
                    "director",
                    "manager",
                ],
            },

        ],
    },



    # ======================================================
    # SYSTEM
    # ======================================================

    {

        "section": "SYSTEM",

        "items": [

            {
                "name": "Documents",
                "icon": "bi-folder",
                "url": "documents:list",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },


            {
                "name": "Notifications",
                "icon": "bi-bell",
                "url": "notifications:list",

                "roles": [
                    "owner",
                    "manager",
                    "secretary",
                ],
            },

        ],
    },



    # ======================================================
    # ADMINISTRATION
    # ======================================================

    {

        "section": "ADMINISTRATION",

        "items": [

            {
                "name": "Settings Dashboard",
                "icon": "bi-gear-wide-connected",
                "url": "settings_app:dashboard",

                "roles": [
                    "owner",
                ],
            },


            {
                "name": "Company Profile",
                "icon": "bi-building-gear",
                "url": "settings_app:company",

                "roles": [
                    "owner",
                ],
            },


            {
                "name": "System Preferences",
                "icon": "bi-sliders",
                "url": "settings_app:system",

                "roles": [
                    "owner",
                ],
            },


            {
                "name": "Notification Settings",
                "icon": "bi-bell-fill",
                "url": "settings_app:notifications",

                "roles": [
                    "owner",
                ],
            },


            {
                "name": "User Management",
                "icon": "bi-people-fill",
                "url": "accounts:user_list",

                "roles": [
                    "owner",
                ],
            },


            {
                "name": "Admin Panel",
                "icon": "bi-shield-lock",
                "url": "/admin/",

                "roles": [
                    "owner",
                ],
            },

        ],
    },


]