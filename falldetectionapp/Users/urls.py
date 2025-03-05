from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    path('', views.login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register/', views.register_user, name='register'),
    path('register/patient', views.register_patient, name='registerPatient')
     
]