from django.urls import path

from . import views

urlpatterns = [
    path("create", views.ConsultationCreation.as_view(), name="consultation-creation"),
]
