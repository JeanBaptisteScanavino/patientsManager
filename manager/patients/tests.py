from django.test import TestCase

from patients.models import Patients


class PatientCreationTestCase(TestCase):
    def test_i_can_create_a_patient(self):
        Patients.objects.create(
            first_name="Test", last_name="Dummy", email="test.dummy@test.com"
        )
        assert Patients
