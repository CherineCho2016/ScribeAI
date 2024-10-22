from django.db import models

# Might not need this??
class Patient(models.Model):
    name = models.CharField(max_length=120)
    id = models.IntegerField(primary_key=True)