from enum import Enum

from django.db import models

from patients.models import Patients



class Consultations(models.Model):
    VISIT = "VISIT"
    CARE = "CARE"
    OPERATION = "OPERATION"
    CONSULTATION_TYPE_CHOICES = [
            (VISIT, "Visite"),
            (CARE, "Suivi"),
            (OPERATION, "Opération")
    ]

    date = models.DateField(verbose_name="Date")

    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)

    description = models.CharField(verbose_name="description", null=True)

    consultation_type = models.CharField(choices=CONSULTATION_TYPE_CHOICES)

    @classmethod
    def _get_all_consultations(cls, patient_pk):
        consultations = cls.objects.filter(patient__pk = patient_pk)
        return consultations