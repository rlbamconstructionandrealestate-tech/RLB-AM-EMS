from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # ADMINISTRATION
    path("admin/", admin.site.urls),

    # DJANGO AUTHENTICATION
    path("accounts/", include("django.contrib.auth.urls")),

    # ACCOUNTS & CUSTOM AUTHENTICATION
    path("", include("accounts.urls")),

    # DASHBOARD
    path("dashboard/", include("dashboard.urls")),

    # OPERATIONS
    path("equipment/", include("equipment.urls")),
    path("fuel/", include("fuel.urls")),
    path("maintenance/", include("maintenance.urls")),
    path("rentals/", include("rentals.urls")),

    # PROJECT MANAGEMENT
    path("projects/", include("projects.urls")),

    # FINANCE
    path("finance/", include("finance.urls")),

    # BUSINESS & CLIENTS
    path("crm/", include("crm.urls")),
    path("real-estate/", include("real_estate.urls")),

    # HUMAN RESOURCES
    path("employees/", include("employees.urls")),

    # DOCUMENTS & REPORTING
    path("documents/", include("documents.urls")),
    path("reports/", include("reports.urls")),

    # NOTIFICATIONS
    path("notifications/", include("notifications.urls")),

    # SYSTEM SETTINGS
    path("settings/", include("settings_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "core.views.error_404"
handler500 = "core.views.error_500"