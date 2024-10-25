from django.contrib import admin
from .models import JsonPatientRecord

class PatientAdmin(admin.ModelAdmin):
    # Specify the fields you want to display in the admin list view
    list_display = ('data', 'created_at')  # Replace 'data' with the actual field names you want to display

# Register your models here.
admin.site.register(JsonPatientRecord, PatientAdmin)
