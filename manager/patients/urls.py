from django.urls import path

from . import views

urlpatterns = [
    path("search", views.research_patients, name="patients-research"),
    path("", views.PatientsList.as_view(), name="patients-list"),
    path("create", views.PatientsCreation.as_view(), name="patients-creation"),
    path("<int:pk>", views.PatientsDetails.as_view(), name="patients-details"),
    path("update/<int:pk>", views.PatientsUpdate.as_view(), name="patients-update"),
    path("delete/<int:pk>", views.PatientsDelete.as_view(), name="patients-delete"),
    path(
        "consultations/<int:pk>",
        views.PatientsConsultationList.as_view(),
        name="patients-consultations",
    ),
]
