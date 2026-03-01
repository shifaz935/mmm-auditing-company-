from django.db import models
from clients.models import Client

class Document(models.Model):

    DOCUMENT_TYPE_CHOICES = [
        ("Invoice", "Invoice"),
        ("Bank Statement", "Bank Statement"),
        ("Expense File", "Expense File"),
        ("Audit Report", "Audit Report"),
        ("Other", "Other"),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPE_CHOICES
    )

    file = models.FileField(upload_to="audit_documents/")
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document_type} - {self.client.client_name}"
