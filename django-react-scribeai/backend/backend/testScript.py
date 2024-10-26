# import os
# import sys
# import django
import base64


# # Add the backend directory to the Python path
# sys.path.append('C:/ScribeAI/django-react-scribeai/backend')

# # Set the DJANGO_SETTINGS_MODULE environment variable
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# # Initialize Django
# django.setup()

# from scribeai.models import JsonPatientRecord

# def query_patient_records():
#     # Try filtering on the UUID field only:
#     results = JsonPatientRecord.objects.filter(data__contains={'id': 'b8c195d4-0396-fb84-3aa2-57dd23ff5a23'})
#     print(results)

# if __name__ == "__main__":
#     query_patient_records()

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://jharwani:DvuNXzy9tmPPGCsC@cluster0.8f0gv.mongodb.net/')
db = client['JsonPatientDatabase']
collection = db['Collection Placeholder']

# The specific ID to filter by
specific_id = "b0a06ead-cc42-aa48-dad6-841d4aa679fa"

# Query the collection for the specific ID
results = collection.find(
    {"entry.resource.id": specific_id},  # Filter by the specific ID
    {
        'entry.resource.presentedForm.data': 1,  # Get only the 'data' field from 'presentedForm'
    }
)

# Iterate through the cursor to print the 'data' values
for record in results:
    # Access the 'presentedForm' field, which is a list
    if 'entry' in record:
        for entry in record['entry']:
            if 'resource' in entry and 'presentedForm' in entry['resource']:
                for form in entry['resource']['presentedForm']:
                    # Print the 'data' value
                    encoded_string = form.get('data', 'No data found')
                    decoded_bytes = base64.b64decode(encoded_string)
                    decoded_string = decoded_bytes.decode('utf-8')
                    print(decoded_string)
