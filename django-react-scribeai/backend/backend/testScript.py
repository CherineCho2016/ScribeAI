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
        response = "General Overview: \n"
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
        response += notes[-1]
        return response
        return(response)


    def preopCardiovascular(self, specific_id):
        response = "Cardiovascular Evaluation: \n"
        results = self.collection.find(
        {
            "entry.resource.id": specific_id
        })
        heartRates = []
        diastolicBloodPressures = []
        systolicBloodPressures = []
        for record in results:
        # Access the 'entry' field
            if 'entry' in record:
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Heart rate":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        heartRates.append(resource['valueQuantity']['value'])
                response += "Heart Rate: " + str(heartRates[-1]) + " bpm \n"
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        if "component" in resource:
                            for componentListItem in resource["component"]:
                                codingList = componentListItem.get("code")
                                for item in (codingList.get("coding")):
                                    if item.get("display") == "Diastolic Blood Pressure":
                                        diastolicBloodPressures.append(componentListItem.get("valueQuantity")["value"])

                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        if "component" in resource:
                            for componentListItem in resource["component"]:
                                codingList = componentListItem.get("code")
                                for item in (codingList.get("coding")):
                                    if item.get("display") == "Systolic Blood Pressure":
                                        systolicBloodPressures.append(componentListItem.get("valueQuantity")["value"])
                response += "Blood Pressure: " + str(systolicBloodPressures[-1]) + "/" + str(diastolicBloodPressures[-1]) + " mm[Hg] \n"
                return response

    def preopPulmonary(self, specific_id):
        response = "Pulmonary Evaluation: \n"
        smokingHx = []
        bloodCO2 = []
        results = self.collection.find(
        {
            "entry.resource.id": specific_id
        })
        
        for record in results:
        # Access the 'entry' field
            if 'entry' in record:
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        if "valueCodeableConcept" in resource:
                            if "coding" in resource["valueCodeableConcept"]:
                                for codingListItem in resource["valueCodeableConcept"]["coding"]:
                                    if codingListItem.get("display") == "Former smoker":
                                        smokingHx.append("Patient is a former smoker")

                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Carbon Dioxide":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        bloodCO2.append(resource['valueQuantity']['value'])
        response += "Smoking status: "
        if smokingHx[-1] == "Patient is a former smoker \n":
            response += smokingHx[-1]
        else:
            response += "Patient is not a former smoker \n"
        response += "Most recent patient blood CO2 levels: " + str(bloodCO2[-1]) + " mmol/L \n"
        return response

    def preopInfectiousDisease(self, specific_id):
        response = "Infecious Disease Evaluation: \n"
        hepCScreen = False
        rubellaScreen = False
        varicellaScreen = False
        results = self.collection.find(
        {
            "entry.resource.id": specific_id
        })

        for record in results:
        # Access the 'entry' field
            if 'entry' in record:
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Hepatitis C antibody test":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    hepCScreen = True
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Rubella screening":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    rubellaScreen = True
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Measurement of Varicella-zoster virus antibody":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    varicellaScreen = True
        response += "Hepatitis C Screen = Performed \n" if hepCScreen else "Hepatitis C screen = Not Performed \n"
        response += "Rubella screen = Performed \n" if rubellaScreen else "Rubella screen = Not Performed \n"
        response += "Measurement of Varicella-zoster = Performed \n" if varicellaScreen else "Measurement of Varicella-zoster = Not Performed \n" 
        return response
        return response   
    
    def preopNeuroPsych(self, specific_id):
        response = "Neurology/Psychology Evaluation: \n"
        depressionScreen = False
        anxietyScreen = False
        domesticScreen = False
        substanceUseScreen = False
        alcoholUseScreen = False
        gadScore = -1
        phq2Score = -1
        results = self.collection.find(
        {
            "entry.resource.id": specific_id
        })

        for record in results:
        # Access the 'entry' field
            if 'entry' in record:
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Depression screening (procedure)":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    depressionScreen = True
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Assessment of anxiety (procedure)":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    anxietyScreen = True
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Screening for domestic abuse (procedure)":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    domesticScreen = True

                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Assessment of substance use (procedure)":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    substanceUseScreen = True

                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Assessment using Alcohol Use Disorders Identification Test - Consumption (procedure)":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    alcoholUseScreen = True


                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Generalized anxiety disorder 7 item (GAD-7) total score [Reported.PHQ]":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        gadScore = resource['valueQuantity']['value']

                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Patient Health Questionnaire 2 item (PHQ-2) total score [Reported]":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        phq2Score = resource['valueQuantity']['value']
        response += "Depression screen = Performed \n" if depressionScreen else "Depression screen = Not Performed \n"
        response += "Anxiety screen = Performed \n" if anxietyScreen else "Anxiety screen = Not Performed \n"
        response += "Domestic abuse screen = Performed \n" if domesticScreen else "Domestic abuse screen = Not Performed \n" 
        response += "Substance use screen = Performed \n" if substanceUseScreen else "Substance use screen = Not Performed \n"
        response += "Alcohol abuse screen = Performed \n" if alcoholUseScreen else "Alcohol abuse screen = Not Performed \n" 
        
        if gadScore != -1:
            response += "Generalized anxiety disorder 7 item (GAD-7) total score: " + str(gadScore) + "\n"
        if phq2Score != -1:
            response += "Patient Health Questionnaire 2 item (PHQ-2) total score:  " + str(phq2Score) + "\n"
        return response


    def preopHematologyOncology(self, specific_id):
        results = self.collection.find(
        {
            "entry.resource.id": specific_id
        })
        leukocyteCount = []
        wbcCount = []
        erythrycyteCount = []
        hemoglobinCount = []
        hematocritCount = []
        plateletCount = []
        lipidPanel = False
        cholCount = []
        triglyCount = []
        ldlCount = []
        hdlCount = []
        a1c = []
        bloodGlucose = []

        for record in results:
        # Access the 'entry' field
            if 'entry' in record:
                # Leukocytes
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Leukocytes [#/volume] in Blood by Automated count":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        leukocyteCount.append(resource['valueQuantity']['value'])
                #WBC
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "WBC Auto (Bld) [#/Vol]":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        wbcCount.append(resource['valueQuantity']['value'])
                #Eryth
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Erythrocytes [#/volume] in Blood by Automated count":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        erythrycyteCount.append(resource['valueQuantity']['value'])
                #Hemoglobin
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Hemoglobin [Mass/volume] in Blood":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        hemoglobinCount.append(resource['valueQuantity']['value'])
                # Hematocrit
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Hematocrit [Volume Fraction] of Blood by Automated count":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        hematocritCount.append(resource['valueQuantity']['value'])
                # Platelets
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Platelets [#/volume] in Blood by Automated count":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        plateletCount.append(resource['valueQuantity']['value'])
                #LDL Panel
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Lipid Panel":
                                    # Ensure 'valueQuantity' exists before accessing 'value'
                                    lipidPanel = True
                
                # Cholesterol
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Total Cholesterol":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        cholCount.append(resource['valueQuantity']['value'])
                # Trigly
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Triglycerides":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        triglyCount.append(resource['valueQuantity']['value'])
                # LDL
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Low Density Lipoprotein Cholesterol":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        ldlCount.append(resource['valueQuantity']['value'])
                # HDL
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "High Density Lipoprotein Cholesterol":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        hdlCount.append(resource['valueQuantity']['value'])

                # A1C
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Hemoglobin A1c/Hemoglobin.total in Blood":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        a1c.append(resource['valueQuantity']['value'])
                # Glucose
                for entry in record['entry']:
                    if 'resource' in entry:
                        resource = entry['resource']
                        # Check if 'code' and 'coding' exist in the resource
                        if 'code' in resource and 'coding' in resource['code']:
                            for coding in resource['code']['coding']:
                                # Check if the 'display' matches "Heart rate"
                                if coding.get('display') == "Glucose [Mass/volume] in Blood":
                                    if 'valueQuantity' in resource and 'value' in resource['valueQuantity']:
                                        bloodGlucose.append(resource['valueQuantity']['value'])

                # Initialize response variable
            response = "Hematology/Oncology Evaulation: \n"

            # Check leukocyteCount
            response += "Leukocyte Count: " + str(leukocyteCount[-1]) + " 10*3/uL\n" if len(leukocyteCount) > 0 else ""

            # Check wbcCount
            response += "WBC Count: " + str(wbcCount[-1]) + " 10*3/uL\n" if len(wbcCount) > 0 else ""

            # Check erythrocyteCount
            response += "Erythrocyte Count: " + str(erythrycyteCount[-1]) + " 10*6/uL\n" if len(erythrycyteCount) > 0 else ""

            # Check hemoglobinCount
            response += "Hemoglobin Count: " + str(hemoglobinCount[-1]) + " g/dL\n" if len(hemoglobinCount) > 0 else ""

            # Check hematocritCount
            response += "Hematocrit Count: " + str(hematocritCount[-1]) + " %\n" if len(hematocritCount) > 0 else ""

            # Check plateletCount
            response += "Platelet Count: " + str(plateletCount[-1]) + " 10*3/uL\n" if len(plateletCount) > 0 else ""

            # Check lipidPanel
            if lipidPanel:
                response += "Lipid Panel: Present\n"

            # Check cholCount
            response += "Cholesterol Count: " + str(cholCount[-1]) + " mg/dL\n" if len(cholCount) > 0 else ""

            # Check triglyCount
            response += "Triglycerides Count: " + str(triglyCount[-1]) + " mg/dL\n" if len(triglyCount) > 0 else ""

            # Check ldlCount
            response += "LDL Count: " + str(ldlCount[-1]) + " mg/dL\n" if len(ldlCount) > 0 else ""

            # Check hdlCount
            response += "HDL Count: " + str(hdlCount[-1]) + " mg/dL\n" if len(hdlCount) > 0 else ""

            # Check a1c
            response += "A1C: " + str(a1c[-1]) + " %\n" if len(a1c) > 0 else ""

            # Check bloodGlucose
            response += "Blood Glucose: " + str(bloodGlucose[-1]) + " mg/dL\n" if len(bloodGlucose) > 0 else ""

            # Print the response
            return response

db = DBQuery()
patientID = "b0a06ead-cc42-aa48-dad6-841d4aa679fa"

# db.preopGeneral(patientID)
# db.preopCardiovascular(patientID)
# db.preopPulmonary(patientID)
# db.preopNeuroPsych(patientID)
# db.preopHematologyOncology(patientID)
# db.preopInfectiousDisease(patientID)