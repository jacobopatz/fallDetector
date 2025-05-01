from . import views
from django.urls import path
from . import views


app_name = 'dashBoard'
urlpatterns = [
     path('', views.dashBoard, name='dashBoard'),
     path('dashBoard/receive_sensor_data', views.receive_sensor_data, name='receive_sensor_data'),
     
     
]