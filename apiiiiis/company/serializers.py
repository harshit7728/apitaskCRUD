
from rest_framework import serializers


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    department = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=200)
