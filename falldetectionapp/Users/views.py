from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, patientRegistrationForm
from django.contrib.auth import login

class login(LoginView):
    template_name = 'login.html'


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('')  # Redirect to a dashboard or homepage
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def register_patient(request):
    if request.method == 'POST':
        form = patientRegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('dashBoard')
        else:
            form = patientRegistrationForm()

        return render(request, 'registerPatient.html', {'form': form})
