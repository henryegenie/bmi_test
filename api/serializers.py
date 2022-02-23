#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import RiskParam, SupportedApp, SupportedAppParam, RiskRecomendation


class RiskParamSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return RiskParam.objects.create(**validated_data)

    class Meta:
        model = RiskParam
        fields = ('name')


class SupportedAppSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return SupportedApp.objects.create(**validated_data)

    class Meta:
        model = SupportedApp
        fields = ('name')

class SupportedAppParamSerializer(serializers.Serializer):
    app_id = serializers.IntegerField()
    param_id = serializers.IntegerField()
    

    def create(self, validated_data):
        return SupportedAppParam.objects.create(**validated_data)

    class Meta:
        model = SupportedAppParam
        fields = ('name')


class RiskRecomendationSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return RiskRecomendation.objects.create(**validated_data)

    class Meta:
        model = RiskRecomendation
        fields = ('name')
    
