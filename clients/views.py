from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Client

@login_required
def client_list_view(request):
    clients = Client.objects.all()
    return render(request, "clients/client_list.html", {"clients": clients})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Client

@login_required
def add_client_view(request):
    if request.method == "POST":
        Client.objects.create(
            client_name=request.POST.get("client_name"),
            company_name=request.POST.get("company_name"),
            contact_number=request.POST.get("contact_number"),
            audit_type=request.POST.get("audit_type"),
            audit_year=request.POST.get("audit_year"),
            status=request.POST.get("status"),
        )
        return redirect("clients:client_list")


    return render(request, "clients/add_client.html")
@login_required
def edit_client_view(request, client_id):
    client = Client.objects.get(id=client_id)

    if request.method == "POST":
        client.client_name = request.POST.get("client_name")
        client.company_name = request.POST.get("company_name")
        client.contact_number = request.POST.get("contact_number")
        client.audit_type = request.POST.get("audit_type")
        client.audit_year = request.POST.get("audit_year")
        client.status = request.POST.get("status")
        client.save()
        return redirect("clients:client_list")

    return render(request, "clients/edit_client.html", {"client": client})

@login_required
def delete_client_view(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect("clients:client_list")
