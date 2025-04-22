from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def receive_alert(request):
    data = request.data
    print("Received Alert:", data)
    
    return Response({'status': 'alert received', 'data': data}, status=status.HTTP_200_OK)
