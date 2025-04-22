from django.urls import path
from . import views

urlpatterns = [
    path('alert/', views.receive_alert, name='alert'),
]
