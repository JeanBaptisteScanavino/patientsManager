from django.core.exceptions import FieldError
from django.db import models
from encrypted_fields import fields


class Patients(models.Model):
    first_name = fields.EncryptedCharField(verbose_name="Prénom")

    last_name = fields.EncryptedCharField(verbose_name="Nom")

    email = fields.EncryptedEmailField(verbose_name="Email")

    adress = models.CharField(verbose_name="Adresse", null=True)

    zip_code = models.CharField(verbose_name="Code Postal", max_length=10, null=True)

    city = models.CharField(
        verbose_name="Ville",
        max_length=255,
        null=True,
    )

    @classmethod
    def check_existing_email(cls, email):
        all_email = cls.objects.values_list("email", flat=True)
        if email in all_email:
            raise FieldError("Email already exist")

    @classmethod
    def _get_all(cls):
        return cls.objects.all()

    @classmethod
    def _create_patient(cls, data):
        patient = cls.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            adress=data["adress"],
            city=data["city"],
            zip_code=data["zip_code"],
        )
        patient.save()
        return patient


class Meta:
    verbose_name = "Patient"


def __str__(self):
    return f"{self.first_name}"
