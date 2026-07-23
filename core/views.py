from django.shortcuts import render



# =====================================================
# 400 BAD REQUEST
# =====================================================

def error_400(request, exception):

    context = {

        "error_code": "400",

        "error_title": "Bad Request",

        "error_message":
            "The request sent to the server could not be processed.",

    }


    return render(

        request,

        "errors/400.html",

        context,

        status=400

    )






# =====================================================
# 403 FORBIDDEN
# =====================================================

def error_403(request, exception):

    context = {

        "error_code": "403",

        "error_title": "Access Denied",

        "error_message":
            "You do not have sufficient permission to access this page.",

    }


    return render(

        request,

        "errors/403.html",

        context,

        status=403

    )







# =====================================================
# 404 PAGE NOT FOUND
# =====================================================

def error_404(request, exception):

    context = {

        "error_code": "404",

        "error_title": "Page Not Found",

        "error_message":
            "The page you are looking for does not exist or has been moved.",

    }


    return render(

        request,

        "errors/404.html",

        context,

        status=404

    )







# =====================================================
# 500 SERVER ERROR
# =====================================================

def error_500(request):

    context = {

        "error_code": "500",

        "error_title": "Internal Server Error",

        "error_message":
            "Something unexpected happened. Our technical team has been notified.",

    }


    return render(

        request,

        "errors/500.html",

        context,

        status=500

    )