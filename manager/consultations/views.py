from consultations.forms import ConsultationCreationForm
from consultations.models import Consultations
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class ConsultationCreation(LoginRequiredMixin, FormView):
    model = Consultations
    form_class = ConsultationCreationForm
    template_name = "consultations/creation.html"
    success_url = reverse_lazy("patients-list")

    def form_valid(self, form):
        Consultations._create_consultation(form.cleaned_data)
        return super(ConsultationCreation, self).form_valid(form)
