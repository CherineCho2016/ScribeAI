from django.db import models
from scribeai.models import JsonPatientRecord  # Adjust this import according to your app name

# Define the patient ID you're looking for
patient_id = "b8c195d4-0396-fb84-3aa2-57dd23ff5a23"

# Query the JsonPatientRecord model for the specific patient's records
results = JsonPatientRecord.objects.filter(
    data__entry__resource__id=patient_id,
    data__entry__resource__resourceType="documentReference"
)

# Process the results
for record in results:
    print(record.data)