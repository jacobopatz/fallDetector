from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from API.models import Message





def dashBoard(request):
    print(Message.objects.exists())
    if(Message.objects.exists()):
        message = Message.objects.all()[0]
    else:
        message = "Hello!"
    
 
    return render(request, 'dashBoard.html',{'message': message})

