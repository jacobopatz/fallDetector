from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tzlocal import get_localzone
from pytz import timezone as pytimezone
import requests

import smtplib
from email.message import EmailMessage
from datetime import datetime,timezone

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
                # msg.set_content(f"Fall detected at {data['timestamp']}")
                # Parse the ISO timestamp into a datetime object
                dt = datetime.fromisoformat(data['timestamp'])

                # Format it to a friendly string (you can customize this format)
                formatted_time = dt.strftime("%Y-%m-%d %I:%M %p (UTC)")

                # Now send the nicely formatted time in the email
                msg.set_content(f"Fall detected at {formatted_time}")

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


@api_view(['GET'])
def check_fall_status(request):
    local_tz = get_localzone()
    latest = FallEvent.objects.order_by('-timestamp').first()
    if latest:
        pacific = pytimezone('America/Los_Angeles')
        pacific_time = latest.timestamp.astimezone(pacific)
        return Response({
            'has_fallen': latest.has_fallen,
            'timestamp': pacific_time.isoformat()
        })
    else:
        return Response({'has_fallen': False, 'timestamp': None})


def clear_fall(request):
    if request.method == 'POST':
        fall_event = FallEvent.objects.create(
            timestamp=datetime.now(timezone.utc),
            has_fallen=False
        )
        return redirect('dashBoard:dashBoard')
    return render(request, 'dashBoard.html', context={})

    # return Response({
    #     'status': 'cleared',
    #     'id': fall_event.id,
    #     'timestamp': fall_event.timestamp,
    #     'has_fallen': fall_event.has_fallen
    # }, status=201)
@api_view(['GET'])
def delete_all_falls(request):
    FallEvent.objects.all().delete()
    return Response({'status': 'all fall events deleted'})

@api_view(['GET'])
def get_all_falls(request):
    allObjects =FallEvent.objects.all()
    serializer = FallEventSerializer(allObjects, many=True)
    return Response({'entries': serializer.data})