from django.core.exceptions import FieldError
from django.test import TestCase
from patients.models import Patients


class PatientCreationTestCase(TestCase):
    def test_i_can_create_a_patient(self):
        Patients.objects.create(
            first_name="Test", last_name="Dummy", email="test.dummy@test.com"
        )
        assert Patients


class PatientDeleteTestCase(TestCase):
    def setUp(self):
        Patients.objects.create(
            first_name="Test", last_name="Dummy", email="test.dummy@test.com"
        )

    def test_i_can_delete_a_patient(self):
        patients = Patients.objects.all()
        assert len(patients) == 1
        assert patients[0].first_name == "Test"

        patients[0].delete()
        patients = Patients.objects.all()
        assert len(patients) == 0


class PatientUpdateTestCase(TestCase):
    def setUp(self):
        Patients.objects.create(
            first_name="Test", last_name="Dummy", email="test.dummy@test.com"
        )

    def test_i_can_update_a_patient(self):
        patients = Patients.objects.all()
        assert len(patients) == 1
        assert patients[0].first_name == "Test"
        assert patients[0].last_name == "Dummy"

        patients[0].last_name = "NotDummy"
        patients[0].save()
        patients = Patients.objects.all()
        assert patients[0].first_name == "Test"
        assert patients[0].last_name == "NotDummy"


class PatientCheckMailCase(TestCase):
    def setUp(self):
        Patients.objects.create(
            first_name="Test", last_name="Dummy", email="test.dummy@test.com"
        )

    def test_search_existing_email_shoud_return_true(self):
        with self.assertRaises(FieldError):
            Patients.check_existing_email("test.dummy@test.com")

    def test_search_new_email_shoud_return_true(self):
        assert not Patients.check_existing_email("not.test.dummy@test.com")


class PatientSearchCase(TestCase):
    def setUp(self):
        Patients.objects.create(
            first_name="Test", last_name="Dummy", email="check@mail.com"
        )
        Patients.objects.create(first_name="Foo", last_name="Test", email="baz@baz.com")
        Patients.objects.create(
            first_name="Shinji", last_name="Ikari", email="eva@001.com"
        )

    def test_search_rei_should_have_no_result(self):
        patients = Patients._search_patients("rei")
        assert len(patients) == 0

    def test_search_should_find_first_name(self):
        patients = Patients._search_patients("shinji")
        assert len(patients) == 1
        assert patients[0].last_name == "Ikari"

    def test_search_should_find_first_name_and_last_name(self):
        patients = Patients._search_patients("test")
        assert len(patients) == 2

    def test_search_should_find_mail(self):
        patients = Patients._search_patients("baz")
        assert len(patients) == 1
        assert patients[0].first_name == "Foo"
