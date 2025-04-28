from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

import smtplib
from email.message import EmailMessage

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

        has_fallen = data['has_fallen']

        if has_fallen:
            # Forward to Alert App
            try:
                requests.post('http://localhost:8000/alert/', json=data)
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] Alert app failed: {e}")

            # Email alert 
            try:
                msg = EmailMessage()
                msg.set_content(f"Fall detected at {data['timestamp']}")
                msg['Subject'] = '🚨 Fall Alert Notification'
                msg['From'] = 'SDSUCS578@gmail.com'
                msg['To'] = 'SDSUCS578@example.com'

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login('SDSUCS578@gmail.com', 'fimc nirl xghh weum')  # Use app password if needed
                    smtp.send_message(msg)

                print("[INFO] Fall alert email sent successfully.")

            except Exception as e:
                print(f"[ERROR] Failed to send fall alert email: {e}")

        # Forward to Dashboard App
        try:
            requests.post('http://localhost:8000/dashBoard/receive_sensor_data', json=data)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Dashboard app failed: {e}")

        return Response({'status': 'success', 'event': data}, status=201)

    return Response({'status': 'failure', 'errors': serializer.errors}, status=400)
