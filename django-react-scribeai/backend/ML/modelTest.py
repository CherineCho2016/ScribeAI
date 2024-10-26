import pandas as pd
import spacy
from spacy.util import minibatch
from spacy.training.example import Example
import random
import re

def findKeywords(text):
    if re.search(r'children', text) != None or re.search(r'child', text) != None:
        return True
    
nlp = spacy.load(r'C:\Users\windows user\Jenny\MSWE\Hackathon\model')

# input
texts = pd.read_csv(r'C:\Users\windows user\Jenny\MSWE\Hackathon\testing.csv')
# texts = texts['text'].tolist()
predicted = []
correct = 0
for index, row in texts.iterrows():
    if findKeywords(row['text']):
        predicted.append('pediatrics')
        if row['category'] == 'pediatrics':
            correct += 1
    else:
        text = row['text']
        doc = nlp.tokenizer(text)
        textcat = nlp.get_pipe('textcat')
        scores = textcat.predict([doc])
        predicted_labels = scores.argmax(axis=1)
        predicted.append(textcat.labels[predicted_labels[0]])
        if textcat.labels[predicted_labels[0]] == row['category']:
            correct += 1

print(predicted)
print("accuracy: ", correct/len(texts))



"""
Why was the patient admitted?
Does the patient have a history of valve disorders, such as aortic stenosis or mitral regurgitation?
Are there any family history factors related to anesthesia reactions or complications?
Has the patient been experiencing any pleuritic chest pain or increased mucus production?
What is the patient’s baseline mental status compared to their current presentation?
Has the patient reported any symptoms like chills, sweats, or rigors?
Are there any additional imaging studies or tests that have been performed recently?
Has the patient had any recent imaging studies (e.g., ultrasound, CT) to assess GI or hepatic issues?
Is the patient on any renal replacement therapy, such as dialysis?
Has the patient reported any changes in appetite, weight, or energy levels that could suggest an endocrine issue?
What medications or supplements is the patient currently taking during the pregnancy?
Has the patient experienced any long-term effects from illnesses or conditions that began in childhood?

"""