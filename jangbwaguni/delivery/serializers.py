from django.core.serializers import serialize
from rest_framework import serializers
from member.models import Rider

# class DeliverySerializer(serializers.ModelSerializer):
class DeliverySerializer(serializers.Serializer):
    class Meta:
        model = Rider
        # fields = ('rider_name, rider_intro')

    # rider_name = Rider.rider_name
    # rider_intro = Rider.rider_intro

#from typing_extensions import required

# class SnippetSerializer(serializers.Serializer):
#     """직렬화/역직렬화 field 정의"""
# 값 검증을 위한 옵션 추가 가능
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template':'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    