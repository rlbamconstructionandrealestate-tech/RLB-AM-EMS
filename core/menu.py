# ==========================================================
# CORE SIDEBAR MENU
# RLB-AM EMS
# ==========================================================


SIDEBAR_MENU = [



    # ==========================================================
    # MAIN
    # ==========================================================

    {
        "section": "MAIN",

        "items": [

            {
                "name": "Dashboard",
                "icon": "bi-speedometer2",
                "url": "accounts:dashboard",
                "roles": ["*"],
            },

        ]
    },







    # ==========================================================
    # OPERATIONS
    # ==========================================================

    {
        "section": "OPERATIONS",

        "items": [



            {
                "name": "Equipment",
                "icon": "bi-truck",
                "url": "equipment:list",

                "roles": [
                    "admin",
                    "manager",
                    "engineer",
                    "equipment",
                    "qs",
                ],
            },




            {
                "name": "Fuel Management",
                "icon": "bi-fuel-pump-fill",
                "url": "fuel:dashboard",

                "roles": [
                    "admin",
                    "manager",
                    "fuel",
                ],
            },





            {
                "name": "Maintenance",
                "icon": "bi-tools",
                "url": "maintenance:dashboard",

                "roles": [
                    "admin",
                    "manager",
                    "engineer",
                ],
            },





            {
                "name": "Rentals",
                "icon": "bi-calendar-check",
                "url": "rentals:dashboard",

                "roles": [
                    "admin",
                    "manager",
                ],
            },






            {
                "name": "Project Dashboard",
                "icon": "bi-speedometer",
                "url": "projects:dashboard",

                "roles": [
                    "admin",
                    "manager",
                    "director",
                    "project_manager",
                ],
            },






            {
                "name": "Projects",
                "icon": "bi-building",
                "url": "projects:list",

                "roles": [
                    "admin",
                    "manager",
                    "director",
                    "engineer",
                    "project_manager",
                    "qs",
                ],
            },



        ],

    },









    # ==========================================================
    # CRM
    # ==========================================================

    {

        "section": "CRM",


        "items": [



            {
                "name": "CRM Dashboard",
                "icon": "bi-people",
                "url": "crm:dashboard",

                "roles": [
                    "admin",
                    "manager",
                    "director",
                    "secretary",
                ],
            },





            {
                "name": "Clients",
                "icon": "bi-person-lines-fill",
                "url": "crm:clients",

                "roles": [
                    "admin",
                    "manager",
                    "secretary",
                ],
            },





            {
                "name": "Contracts",
                "icon": "bi-file-earmark-text",
                "url": "crm:contracts",

                "roles": [
                    "admin",
                    "manager",
                    "director",
                    "secretary",
                ],
            },


        ],

    },









    # ==========================================================
    # FINANCE
    # ==========================================================

    {

        "section": "FINANCE",


        "items": [



            {
                "name": "Finance Dashboard",
                "icon": "bi-bank",
                "url": "finance:dashboard",

                "roles": [
                    "admin",
                    "manager",
                    "finance",
                    "secretary",
                ],
            },






            {
                "name": "Income",
                "icon": "bi-cash-stack",
                "url": "finance:add_income",

                "roles": [
                    "admin",
                    "finance",
                ],
            },






            {
                "name": "Expenses",
                "icon": "bi-wallet2",
                "url": "finance:add_expense",

                "roles": [
                    "admin",
                    "finance",
                ],
            },






            {
                "name": "Invoices",
                "icon": "bi-receipt",
                "url": "finance:add_invoice",

                "roles": [
                    "admin",
                    "finance",
                ],
            },


        ],

    },









    # ==========================================================
    # HUMAN RESOURCES
    # ==========================================================

    {

        "section": "HUMAN RESOURCES",


        "items": [



            {
                "name": "Employees",
                "icon": "bi-person-badge",
                "url": "employees:list",

                "roles": [
                    "admin",
                    "manager",
                    "hr",
                ],
            },





            {
                "name": "Attendance",
                "icon": "bi-calendar2-check",
                "url": "employees:attendance",

                "roles": [
                    "admin",
                    "hr",
                ],
            },






            {
                "name": "Payroll",
                "icon": "bi-wallet",
                "url": "employees:payroll",

                "roles": [
                    "admin",
                    "hr",
                ],
            },


        ],

    },









    # ==========================================================
    # REPORTS
    # ==========================================================

    {

        "section": "REPORTS",


        "items": [



            {
                "name": "Reports",
                "icon": "bi-graph-up",
                "url": "reports:dashboard",

                "roles": [
                    "admin",
                    "manager",
                    "director",
                ],
            },





            {
                "name": "Analytics",
                "icon": "bi-pie-chart",
                "url": "reports:analytics",

                "roles": [
                    "admin",
                    "director",
                ],
            },


        ],

    },









    # ==========================================================
    # SYSTEM
    # ==========================================================

    {

        "section": "SYSTEM",


        "items": [



            {
                "name": "Documents",
                "icon": "bi-folder",
                "url": "documents:list",

                "roles": [
                    "admin",
                    "manager",
                    "secretary",
                ],
            },





            {
                "name": "Notifications",
                "icon": "bi-bell",
                "url": "notifications:list",

                "roles": [
                    "admin",
                    "manager",
                    "director",
                ],
            },


        ],

    },









    # ==========================================================
    # ADMINISTRATION
    # ==========================================================

    {

        "section": "ADMINISTRATION",


        "items": [




            {
                "name": "Settings Dashboard",
                "icon": "bi-gear-wide-connected",
                "url": "settings_app:dashboard",

                "roles": [
                    "admin",
                    "director",
                ],
            },





            {
                "name": "Company Profile",
                "icon": "bi-building-gear",
                "url": "settings_app:company",

                "roles": [
                    "admin",
                    "director",
                ],
            },






            {
                "name": "System Preferences",
                "icon": "bi-sliders",
                "url": "settings_app:system",

                "roles": [
                    "admin",
                    "director",
                ],
            },






            {
                "name": "Notification Settings",
                "icon": "bi-bell-fill",
                "url": "settings_app:notifications",

                "roles": [
                    "admin",
                    "director",
                ],
            },







            {
                "name": "Admin Panel",
                "icon": "bi-shield-lock",
                "url": "/admin/",

                "roles": [
                    "admin",
                ],
            },


        ],

    },


]