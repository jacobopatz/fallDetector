from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2', 'role']

class patientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name','last_name', 'date_of_birth', 'user']
