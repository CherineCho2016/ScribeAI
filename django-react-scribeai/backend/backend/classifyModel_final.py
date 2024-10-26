# backend/classifyModel_final.py
import spacy
import re

# Load the spaCy model from the `model` directory
print("[ClassifyModel] Loading spaCy model")
nlp = spacy.load('./backend/model')
print("[ClassifyModel] Model loaded successfully")

# Function to detect specific keywords
def findKeywords(text):
    print(f"[ClassifyModel] Checking keywords in: {text}")
    result = bool(re.search(r'children|child', text, re.IGNORECASE))
    print(f"[ClassifyModel] Keyword check result: {result}")
    return result

# Classify function that returns a category
def classify(text):
    print(f"[ClassifyModel] Starting classification for: {text}")
    # Check if text contains pediatric-related keywords
    if findKeywords(text):
        print("[ClassifyModel] Pediatric case identified")
        return 'pediatrics'
    else:
        # Tokenize the text and get the textcat pipe from the model
        doc = nlp.tokenizer(text)
        textcat = nlp.get_pipe('textcat')
        scores = textcat.predict([doc])
        predicted_labels = scores.argmax(axis=1)
        category = textcat.labels[predicted_labels[0]]
        print(f"[ClassifyModel] Category identified: {category}")
        return category