from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



@login_required
def dashboard(request):

    context = {

        "total_documents": 0,

        "recent_documents": [],

        "storage_used": 0,

    }


    return render(
        request,
        "documents/dashboard.html",
        context
    )




@login_required
def document_list(request):

    context = {

        "documents": []

    }


    return render(
        request,
        "documents/list.html",
        context
    )




@login_required
def upload_document(request):

    return render(
        request,
        "documents/upload.html"
    )




@login_required
def document_detail(request, pk):

    context = {

        "document_id": pk

    }


    return render(
        request,
        "documents/detail.html",
        context
    )




@login_required
def delete_document(request, pk):

    return redirect(
        "documents:list"
    )