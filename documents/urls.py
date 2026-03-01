from django.urls import path
from . import views

app_name = "documents"

urlpatterns = [
    path("", views.document_list_view, name="document_list"),
    path("upload/", views.upload_document_view, name="upload_document"),
]
