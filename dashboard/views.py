from django.shortcuts import render
from clients.models import Client
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):
    total_clients = Client.objects.count()
    pending_audits = Client.objects.filter(status="Pending").count()
    completed_audits = Client.objects.filter(status="Completed").count()

    context = {
        "total_clients": total_clients,
        "pending_audits": pending_audits,
        "completed_audits": completed_audits
    }

    return render(request, "dashboard/dashboard.html", context)
