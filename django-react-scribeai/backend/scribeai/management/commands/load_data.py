import os
import json
from pymongo import MongoClient
import gridfs

# Connect to MongoDB

client = MongoClient('mongodb+srv://jharwani:DvuNXzy9tmPPGCsC@cluster0.8f0gv.mongodb.net/')
db = client['patients']
collection = db['collection']

fs = gridfs.GridFS(db)

# Path to the folder containing JSON files
folder_path = 'C:/ScribeAI/django-react-scribeai/backend/patientDataFolder/fhir'  # Update this path

# Loop through all JSON files in the directory
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:  # Specify UTF-8 encoding
            data = json.load(f)  # Load JSON data
            # Store the JSON data in GridFS
            fs.put(json.dumps(data).encode('utf-8'), filename=filename)

print('All JSON files have been loaded into the database using GridFS.')
