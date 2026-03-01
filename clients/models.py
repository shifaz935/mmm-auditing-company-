from django.db import models

class Client(models.Model):

    AUDIT_TYPE_CHOICES = [
        ("Accounting", "Accounting"),
        ("Auditing", "Auditing"),
        ("Bookkeeping", "Bookkeeping"),
        ("Tax Consultancy", "Tax Consultancy"),
        ("Feasibility Study", "Feasibility Study"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    client_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=20)

    audit_type = models.CharField(
        max_length=50,
        choices=AUDIT_TYPE_CHOICES
    )

    audit_year = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.company_name}"
