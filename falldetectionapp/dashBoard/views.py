from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from API.models import Message





#TODO: create logic for getting sensor data (either fallen, or not fallen)
@csrf_exempt
@api_view(['POST'])
def receive_sensor_data(request):
    data = request.data

    timestamp = data['timestamp'] #UTC timestamp, when event occured
    has_fallen = data['has_fallen'] #True or False

    print("Received sensor Data:", data)
    return Response({'status': 'sensor data received', 'data': data})

def dashBoard(request):
    print(Message.objects.exists())
    if(Message.objects.exists()):
        message = Message.objects.all()[0]
    else:
        message = "Hello!"
    
 
    return render(request, 'dashBoard.html',{'message': message})

