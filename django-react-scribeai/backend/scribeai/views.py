from rest_framework import generics
from .models import JsonPatientRecord
from .serializers import JsonRecordSerializer

class JsonRecordList(generics.ListCreateAPIView):
    queryset = JsonPatientRecord.objects.all()
    serializer_class = JsonRecordSerializer

class JsonRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JsonPatientRecord.objects.all()
    serializer_class = JsonRecordSerializer