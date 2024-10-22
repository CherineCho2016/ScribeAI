from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientSerializer
from .models import Patient

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()