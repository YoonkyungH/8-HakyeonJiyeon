from django.core.serializers import serialize
from rest_framework import serializers
from .models import Rider

# class DeliverySerializer(serializers.ModelSerializer):
class DeliverySerializer(serializers.Serializer):
    class Meta:
        model = Rider
        # fields = ('rider_name, rider_intro')
    # rider_name = Rider.rider_name
    # rider_intro = Rider.rider_intro
