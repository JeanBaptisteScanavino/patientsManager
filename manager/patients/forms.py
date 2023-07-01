from django import forms


class PatientsCreationForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=100)
    last_name = forms.CharField(label="Nom", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    adress = forms.CharField(label="Adress", max_length=300)
    zip_code = forms.CharField(label="Code Postal")
    city = forms.CharField(label="ville", max_length=200)
