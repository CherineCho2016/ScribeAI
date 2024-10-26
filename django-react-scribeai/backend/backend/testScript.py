# import os
# import sys
# import django
import base64
from pymongo import MongoClient

class DBQuery():
    
    def __init__(self):
        # Connect to MongoDB
        self.client = MongoClient('mongodb+srv://jharwani:DvuNXzy9tmPPGCsC@cluster0.8f0gv.mongodb.net/')
        self.db = self.client['JsonPatientDatabase']
        self.collection = self.db['Collection Placeholder']

    def base64Convert(self, str64):
        decoded_bytes = base64.b64decode(str64)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string

    def preopGeneral(self, specific_id):
        results = self.collection.find(
            {"entry.resource.id": specific_id},  # Filter by the specific ID
            {
                'entry.resource.presentedForm.data': 1,  # Get only the 'data' field from 'presentedForm',    # Get effectiveDateTime
            }
        ).sort("entry.resource.effectiveDateTime", -1).limit(1)  # Sort by effectiveDateTime

        # Iterate through the cursor to print the 'data' values
        notes = []
        for record in results:
            # Access the 'entry' field
            if 'entry' in record:
                for entry in record['entry']:
                    if 'resource' in entry:

                    # Check for presentedForm and print data
                        
                        if 'presentedForm' in entry['resource']:
                            for form in entry['resource']['presentedForm']:
                                encoded_string = form.get('data', 'No data found')
                                decoded_string = self.base64Convert(encoded_string)
                                notes.append(decoded_string)
        return notes[-1]

    def preopCardiovascular(self, specific_id):
        
        results = self.collection.find(
        {
            "entry.resource.id": specific_id,
            "entry.resource.code.coding.display": "Heart rate"  # Filter for entries where the display is "Heart rate"
        },
        {
            'entry.resource.valueQuantity': 1  # Include only the 'valueQuantity' field in the results
        }
    )
        for record in results:
            # Access the 'entry' field
            if 'entry' in record:
                for entry in record['entry']:
                    if 'resource' in entry:

                    # Check for presentedForm and print data
                        
                        if 'valueQuantity' in entry['resource']:
                            valueQuantity = entry['resource']['valueQuantity']
                            hr = valueQuantity.get('value', 'No data found')
                            print(hr)


db = DBQuery()
patientID = "b0a06ead-cc42-aa48-dad6-841d4aa679fa"
# db.preopGeneral(patientID)
db.preopCardiovascular(patientID)