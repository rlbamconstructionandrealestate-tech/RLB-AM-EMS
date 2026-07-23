from .models import Notification



def notifications(request):

    if not request.user.is_authenticated:

        return {}


    return {

        "unread_notifications_count":
            Notification.objects.filter(
                user=request.user,
                is_read=False
            ).count(),


        "latest_notifications":
            Notification.objects.filter(
                user=request.user
            )[:5],

    }