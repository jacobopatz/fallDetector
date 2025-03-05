from . import views
from django.urls import path




urlpatterns = [
     path('API/receive_message', views.receive_message, name='receive_message'),
     
]