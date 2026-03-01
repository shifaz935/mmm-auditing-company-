from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Document,Client

@login_required
def document_list_view(request):
    documents = Document.objects.all()
    return render(request, "documents/document_list.html", {
        "documents": documents
    })
from django.shortcuts import render, redirect
@login_required
def upload_document_view(request):
    if request.method == "POST":
        Document.objects.create(
            client_id=request.POST.get("client"),
            document_type=request.POST.get("document_type"),
            file=request.FILES.get("file"),
        )
        return redirect("documents:document_list")

    clients = Client.objects.all()
    return render(request, "documents/upload_document.html", {"clients": clients})
