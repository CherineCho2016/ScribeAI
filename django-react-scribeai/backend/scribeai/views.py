from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientSerializer
from .models import Patient

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")
# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()