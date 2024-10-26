# backend/switch_logic.py
from testScript import DBQuery  # Import DBQuery class from testScript
from classifyModel_final import classify  # Import classify function from classify_model
import classifyModel_final
# Instantiate DBQuery
db_query = DBQuery()
patientID = "b0a06ead-cc42-aa48-dad6-841d4aa679fa"

# Switch function to execute the right query based on the case
def switch(case):
    # Define a dictionary with case options, mapping cases to DBQuery methods
    switch_dict = {
        "general": lambda: db_query.preopGeneral(patientID),
        "cardiovascular": lambda: db_query.preopCardiovascular(patientID),
        "pulmonary": lambda: db_query.preopPulmonary(patientID),
        "neurology": lambda: db_query.preopNeuroPsych(patientID),
        "hematology": lambda: db_query.preopHematologyOncology(patientID),
        "infectious_disease": lambda: db_query.preopInfectiousDisease(patientID),
        # Add pediatrics handling if required by your project logic
        "pediatrics": lambda: "Pediatrics query - No data fetch logic defined."
    }

    # Default case if classification does not match any key
    default = lambda: "Default case result: No matching case found."

    # Get the result based on the case, or use default if case not found
    return switch_dict.get(case, default)()

# Function to classify text and fetch results based on the classification
def classify_and_fetch(text):
    # Get the category by classifying the input text
    category = classify(text)
    print(f"Classified category: {category}")
    
    # Pass the category to the switch function to get the relevant data
    result = switch(category)
    
    # Return the result from the switch function
    return result

# Example usage
if __name__ == "__main__":
    text = "Are there any signs of reduced blood flow, such as cold extremities or weak pulses?"
    result = print(classify_and_fetch(text))
    # print("Result from DB Query:", result)
