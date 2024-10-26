import spacy
import re

def findKeywords(text):
    if re.search(r'children', text) != None or re.search(r'child', text) != None:
        return True
##change the path to the model
nlp = spacy.load(r'.\model')

##classify function
##input: question
##output: category
def classify(text):
    if findKeywords(text):
        return 'pediatrics'
    else:
        doc = nlp.tokenizer(text)
        textcat = nlp.get_pipe('textcat')
        scores = textcat.predict([doc])
        predicted_labels = scores.argmax(axis=1)
        return textcat.labels[predicted_labels[0]]

##example
##print(classify("How is the patient's overall condition?"))
#output: 'general'

