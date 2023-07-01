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
    def _get_all(cls):
        return cls.objects.all()

    # TODO create patient

class Meta:
    verbose_name = "Patient"


def __str__(self):
    return f"{self.pk}"
