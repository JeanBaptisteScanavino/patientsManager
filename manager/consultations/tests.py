from consultations.models import Consultations
from django.test import TestCase
from patients.models import Patients


class ConsultationCreationTestCase(TestCase):
    def setUp(self):
        Patients.objects.create(
            first_name="Test", last_name="Dummy", email="test.dummy@test.com"
        )

    def test_i_can_create_a_consultation(self):
        patients = Patients.objects.all()
        Consultations.objects.create(
            date="2023-12-30",
            patient=patients[0],
            description="my description",
            consultation_type="VISIT",
        )
        assert Consultations
