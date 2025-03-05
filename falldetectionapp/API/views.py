from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message
# Create your views here.
@api_view(['POST'])

def receive_message(request):
    if request.method == 'POST':
        # Get the plain text message from the body
        message = request.data.get('message', '')

        
        if message:
            Message.objects.all().delete()
            Message.objects.create(content=message)
            print(message)
            
            return Response({'status': 'success', 'message_received': message}, status=200)

        else:
            return Response({'status': 'failure', 'message': 'No message received'}, status=400)


