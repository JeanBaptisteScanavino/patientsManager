from consultations.models import Consultations
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# Create your views here.
class ConsultationCreation(CreateView):
    model = Consultations
    # form_class = PatientsCreationForm
    fields = ["date", "patient", "description", "consultation_type"]
    template_name = "consultations/creation.html"
    success_url = reverse_lazy("patients-list")
