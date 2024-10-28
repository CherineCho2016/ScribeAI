**Scribe AI**


**Problem Statement**
- Retrieving critical and relevant data from Electronic Health Records can be an incredibly arduous task containing decades of encounters and multiple sources of information.
- Reduce friction between physicians and EHR software.

**Solution**
- Full-stack software that takes physician input and uses a Machine Learning model to     perform a classification task.
- Relevant information is pulled from the database and returned to the physician.

- Frontend
  - React.js,  Socket.io
- Backend
  - Django, MongoDB, Azure, PyMongo
- ML Model
  - Spacy (SVM)
  - NLP Text Categorizer


Start Backend
- install all requred libraries
- cd django-react-scribeai/backend
- daphne backend.asgi:application -p 8000


Start Frontend
- cd into /django/frontend
- npm i
- run npm start

![image](https://github.com/user-attachments/assets/2de26fa2-d8f0-4be6-9174-67b86a23868d)

