from django.db import models

# Create your models here.


class Patients(models.Model):
    first_name = models.CharField(verbose_name="Prénom")

    last_name = models.CharField(verbose_name="Nom")

    email = models.EmailField(verbose_name="Email", unique=True)

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

    @classmethod
    def _create_patient(cls, data):
        patient = cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            adress=data["adress"],
            zip_code=data["zip_code"],
            city=data["city"],
        )
        patient.save()


class Meta:
    verbose_name = "Patient"


def __str__(self):
    return f"{self.pk}"
