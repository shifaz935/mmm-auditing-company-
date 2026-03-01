from django.urls import path
from . import views

app_name = "clients"

urlpatterns = [
    path("", views.client_list_view, name="client_list"),
    path("add/", views.add_client_view, name="add_client"),
    path("edit/<int:client_id>/", views.edit_client_view, name="edit_client"),
    path("delete/<int:client_id>/", views.delete_client_view, name="delete_client"),
]
