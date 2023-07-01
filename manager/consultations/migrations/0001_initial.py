# Generated by Django 4.2.2 on 2023-07-01 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consultations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="Date")),
                (
                    "description",
                    models.CharField(null=True, verbose_name="description"),
                ),
                (
                    "consultation_type",
                    models.CharField(
                        choices=[
                            ("VISIT", "Visite"),
                            ("CARE", "Suivi"),
                            ("OPERATION", "Opération"),
                        ]
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.patients",
                    ),
                ),
            ],
        ),
    ]