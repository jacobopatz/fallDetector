from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import Message, FallEvent
from .serializers import FallEventSerializer

@api_view(['POST'])
def receive_message(request):
    """
    Handles two types of POST payloads:
    1. Plain 'message' text (for debug/UI test).
    2. Fall detection JSON: {'timestamp': ..., 'has_fallen': ...}.
    """

    # --- Handle plain text message ---
    message = request.data.get('message', None)
    if message:
        Message.objects.all().delete()
        Message.objects.create(content=message)
        print(f"Message received: {message}")
        return Response({'status': 'success', 'message_received': message}, status=200)

    # --- Handle structured fall event data ---
    serializer = FallEventSerializer(data=request.data)
    if serializer.is_valid():
        fall_event = serializer.save()
        data = serializer.data  # {'timestamp': ..., 'has_fallen': ...}

        # Forward to Alert App
        try:
            requests.post('http://localhost:8001/alert', json=data)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Alert app failed: {e}")

        # Forward to Dashboard App
        try:
            requests.post('http://localhost:8002/dashboard', json=data)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Dashboard app failed: {e}")

        return Response({'status': 'success', 'event': data}, status=201)

    return Response({'status': 'failure', 'errors': serializer.errors}, status=400)
