from django.urls import path
from . import views

urlpatterns = [
    path('API/receive_message/', views.receive_message, name='receive_message'),
    path('API/check-fall/', views.check_fall_status, name='check_fall_status'),
    path('API/clear-fall/', views.clear_fall, name='clear_fall_status')

]
