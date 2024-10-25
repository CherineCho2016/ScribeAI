from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

# Register your models here.

admin.site.register(Patient, PatientAdmin)