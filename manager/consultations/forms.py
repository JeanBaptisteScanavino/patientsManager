from consultations.models import Consultations
from django import forms


class ConsultationCreationForm(forms.ModelForm):
    class Meta:
        model = Consultations
        fields = "__all__"
