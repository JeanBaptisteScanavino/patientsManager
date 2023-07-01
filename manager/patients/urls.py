from django.urls import path

from . import views

urlpatterns = [
    path("", views.PatientsList.as_view(), name="patients-list"),
    path("create", views.PatientsCreation.as_view(), name="patients-creation"),
    path("<int:pk>", views.PatientsDetails.as_view(), name="patients-details"),
    path("update/<int:pk>", views.PatientsUpdate.as_view(), name="patients-update"),
    path("delete/<int:pk>", views.PatientsDelete.as_view(), name="patients-delete"),
]
