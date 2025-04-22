from rest_framework import serializers
from .models import FallEvent

class FallEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FallEvent
        fields = ['timestamp', 'has_fallen']
