from rest_framework import serializers
from .models import Company, Department, CustomUser, upload


from rest_framework import serializers

from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'company']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'department']


class uploadserial(serializers.ModelSerializer):
    class Meta:
        model = upload
        fields = ['name', 'rdoc']
