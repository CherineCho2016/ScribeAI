from rest_framework import serializers
from .models import JsonPatientRecord

class JsonRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonPatientRecord
        fields = '__all__'