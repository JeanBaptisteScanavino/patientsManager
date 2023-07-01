from faker import Faker
from patients.models import Patients
fake = Faker()


# python manage.py runscript create_some_patients --script-args <int>
def run(*args):
    print('START the creation')
    for n in range(int(args[0])):
        name = (fake.name()).split(' ')
        email = f'{name[0]}.{name[1]}@test.com'
        patient = Patients(
            first_name = name[0],
            last_name = name[1],
            email = email
        )
        patient.save()
    print("END of creation")


