from django.db import models

# Might not need this??
class JsonPatientRecord(models.Model):
    data = models.JSONField()  # Stores JSON data as a dictionary
    created_at = models.DateTimeField(auto_now_add=True)