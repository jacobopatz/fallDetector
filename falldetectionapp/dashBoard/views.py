from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from API.models import FallEvent  

@csrf_exempt
@api_view(['POST'])
def receive_sensor_data(request):
    data = request.data

    timestamp = data['timestamp']  # UTC timestamp
    has_fallen = data['has_fallen']  # True or False

    print("Received sensor Data:", data)
    return Response({'status': 'sensor data received', 'data': data})

def dashBoard(request):
    if FallEvent.objects.exists():
        message = FallEvent.objects.latest('timestamp')  
    else:
        message = None

    return render(request, 'dashBoard.html', {'message': message})

