# Model/classify_model.py
import spacy
import re

# Load the spaCy model from the `model` directory
nlp = spacy.load('./model')

# Function to detect specific keywords
def findKeywords(text):
    return bool(re.search(r'children|child', text, re.IGNORECASE))

# Classify function that returns a category
def classify(text):
    # Check if text contains pediatric-related keywords
    if findKeywords(text):
        print("here")
        return 'pediatrics'
    else:
        # Tokenize the text and get the textcat pipe from the model
        doc = nlp.tokenizer(text)
        textcat = nlp.get_pipe('textcat')
        scores = textcat.predict([doc])
        predicted_labels = scores.argmax(axis=1)
        print("here")
        return textcat.labels[predicted_labels[0]]
