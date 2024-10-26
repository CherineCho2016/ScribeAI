from flask import Flask, request, jsonify
import pandas as pd
import spacy
import re

app = Flask(__name__)
@app.route("/predict", methods=['POST'])

def predict():
    data = request.get_json()
    question = data.get('question', '')

    def findKeywords(text):
        if re.search(r'children', text) != None or re.search(r'child', text) != None:
            return True
        
    nlp = spacy.load(r'C:\Users\windows user\Jenny\MSWE\Hackathon\model')

    if findKeywords(question):
        response = {
        'question': question,
        'predicted_labels': 'pediatrics'
    }
    else:
        doc = nlp.tokenizer(question)
        textcat = nlp.get_pipe('textcat')
        scores = textcat.predict([doc])
        predicted_labels = scores.argmax(axis=1)
        response = {
            'question': question,
            'predicted_labels': textcat.labels[predicted_labels[0]]
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)