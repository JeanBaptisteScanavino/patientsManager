from consultations.models import Consultations
from django import forms
from django_select2.forms import ModelSelect2Widget
from patients.models import Patients


class ConsultationCreationForm(forms.Form):
    date = forms.DateField(label="Date")
    patient = forms.ChoiceField(
        widget=ModelSelect2Widget(
            url="patients-research",
        )
    )
    # patient = forms.ModelChoiceField(queryset=Patients.objects.all())
    patient = forms.ChoiceField()

    description = forms.CharField(label="Description")
    consultation_type = forms.ChoiceField(
        choices=Consultations.CONSULTATION_TYPE_CHOICES
    )
