from consultations.models import Consultations
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import FieldError
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView, UpdateView
from patients.forms import PatientsCreationForm
from patients.models import Patients


class PatientsList(LoginRequiredMixin, ListView):
    model = Patients
    template_name = "patients/list.html"
    paginate_by = 50


class PatientsCreation(LoginRequiredMixin, FormView):
    model = Patients
    form_class = PatientsCreationForm
    template_name = "patients/creation.html"
    success_url = reverse_lazy("patients-list")

    def is_valid(self, form):
        try:
            Patients.check_existing_email(form.cleaned_data["email"])
            return True
        except FieldError as e:
            raise e

    def form_valid(self, form):
        try:
            self.is_valid(form)
            Patients._create_patient(form.cleaned_data)
            return super(PatientsCreation, self).form_valid(form)
        except Exception as e:
            return HttpResponseBadRequest(e)


class PatientsDetails(LoginRequiredMixin, DetailView):
    model = Patients
    template_name = "patients/detail.html"


class PatientsUpdate(LoginRequiredMixin, UpdateView):
    model = Patients
    fields = ["first_name", "last_name", "email", "adress", "zip_code", "city"]
    template_name = "patients/patients_update.html"
    success_url = reverse_lazy("patients-list")


class PatientsDelete(LoginRequiredMixin, DeleteView):
    model = Patients
    template_name = "patients/patients_confirm_delete.html"
    success_url = reverse_lazy("patients-list")


class PatientsConsultationList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template_name = "consultations/list.html"
        context = {}
        context["consultations"] = Consultations._get_all_consultations(kwargs["pk"])
        return render(request, template_name, context)


@login_required
def research_patients(request):
    if request.method == "GET":
        template_name = "patients/list.html"
        data = Patients._search_patients(request.GET.get("search"))
        context = {}
        context["page_obj"] = data
        return render(request, template_name, context)
