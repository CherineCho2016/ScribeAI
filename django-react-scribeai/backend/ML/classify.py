import pandas as pd
import spacy
from spacy.util import minibatch
from spacy.training.example import Example
import random

# Loading the spam data
# ham is the label for non-spam messages
train = pd.read_csv(r'C:\Users\windows user\Jenny\MSWE\Hackathon\training.csv')
print(train.head(5))

# Create an empty model
nlp = spacy.blank("en")

# Add the TextCategorizer to the empty model
textcat = nlp.add_pipe("textcat")
# Add labels to text classifier
textcat.add_label("general")
textcat.add_label("cardiovascular")
textcat.add_label("anesthesia")
textcat.add_label("pulmonary")
textcat.add_label("neuro psych")
textcat.add_label("infectious disease")
textcat.add_label("hematology")
textcat.add_label("gi or hepatic")
textcat.add_label("renal")
textcat.add_label("endocrinology")
textcat.add_label("pregnancy")
textcat.add_label("pediatrics")

train_texts = train['text'].values
train_labels = [{'cats': {'general': label == 'general',
                          'cardiovascular': label == 'cardiovascular',
                          'anesthesia': label == 'anesthesia',
                          'pulmonary': label == 'pulmonary',
                          'neuro psych': label == 'neuro psych',
                          'infectious disease': label == 'infectious disease',
                          'hematology': label == 'hematology',
                          'gi or hepatic': label == 'gi or hepatic',
                          'renal': label == 'renal',
                          'endocrinology': label == 'endocrinology',
                          'pregnancy': label == 'pregnancy',
                          'pediatrics': label == 'pediatrics',}} 
                for label in train['label']]

train_data = list(zip(train_texts, train_labels))
train_data[:3]

spacy.util.fix_random_seed(1)
optimizer = nlp.begin_training()

# Create the batch generator with batch size = 8
batches = minibatch(train_data, size=16)
# Iterate through minibatches
for batch in batches:
    # Each batch is a list of (text, label) 
    for text, labels in batch:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, labels)
        nlp.update([example], sgd=optimizer)
        
random.seed(1)
spacy.util.fix_random_seed(1)
optimizer = nlp.begin_training()

losses = {}
for epoch in range(10):
    random.shuffle(train_data)
    # Create the batch generator with batch size = 8/16
    batches = minibatch(train_data, size=16)
    # Iterate through minibatches
    for batch in batches:
        for text, labels in batch:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, labels)
            nlp.update([example], sgd=optimizer, losses=losses)
    print(losses)    

# Save the model to disk
output_dir = r'C:\Users\windows user\Jenny\MSWE\Hackathon\model'
nlp.to_disk(output_dir)
print(f"Model saved to {output_dir}")


"""
# input
texts = ["Does the patient have a history of valve disorders, such as aortic stenosis or mitral regurgitation?",
         "Is there any issues with the patient’s kidneys?" ]
docs = [nlp.tokenizer(text) for text in texts]
    
# Use textcat to get the scores for each doc
textcat = nlp.get_pipe('textcat')
scores = textcat.predict(docs)

print(scores)

# From the scores, find the label with the highest score/probability
predicted_labels = scores.argmax(axis=1)
print([textcat.labels[label] for label in predicted_labels])

"""
