from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from patients.forms import PatientsCreationForm
from patients.models import Patients


class PatientsList(View):
    def get(self, request, *args, **kwargs):
        template_name = "patients/list.html"
        context = {}
        context["patients"] = Patients._get_all()
        return render(request, template_name, context)


class PatientsCreation(CreateView):
    model = Patients
    form_class = PatientsCreationForm
    fields = ["first_name", "last_name", "email", "adress", "zip_code", "city"]
    template_name = "patients/creation.html"
    success_url = reverse_lazy("patients-list")


class PatientsDetails(DetailView):
    model = Patients
    template_name = "patients/detail.html"


class PatientsUpdate(UpdateView):
    model = Patients
    fields = ["first_name", "last_name", "email", "adress", "zip_code", "city"]
    template_name = "patients/patients_update.html"
    success_url = reverse_lazy("patients-list")


class PatientsDelete(DeleteView):
    model = Patients
    template_name = "patients/patients_confirm_delete.html"
    success_url = reverse_lazy("patients-list")
