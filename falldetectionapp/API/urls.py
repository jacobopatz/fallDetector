from django.urls import path
from . import views

urlpatterns = [
    path('API/receive_message/', views.receive_message, name='receive_message'),
]
