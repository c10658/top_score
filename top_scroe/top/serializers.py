from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client', 'score')

    def validate(self, attrs):
        if attrs.__contains__('score'):
            if attrs['score'] < 1 or attrs['score'] > 10000000:
                raise serializers.ValidationError('分数范围需在1-10000000之间')
        return attrs

