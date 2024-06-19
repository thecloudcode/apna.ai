# What's happening here?

<<<<<<< HEAD
=======
Hosted : https://apna-ai-wsfp.onrender.com

>>>>>>> 19c09e64ceda5a78df2765b4624657717919dbc5
### Chat with your Resume
#### Author : Yashwanth
This is the backend for Resume AI where the `app.py` file uses PyPDF2 to extract the text data from the pdf, Google Gemini API Model to interact with the user, given the context of the Resume. Moreover, it uses LangChain to create an end-to-end pipeline for smooth processing of the model.

`FAISS` : This is used to index the embeddings of the text chunks, and create a vector store

### Database
#### Author : Akshaya
This contains a `__init__`.py file to create a SUPABASE CLIENT

Then each `.py` file is named after the corresponding table and contains endpoints to connect to the database. The file also creates a blueprint which can be imported in `app.py` to call the endpoints

The `app.py` calls all the blueprints from each `.py` file and becomes a single source of endpoint call

### Keerthi-Chatbot
#### Author : Keerthi
This is an interactive chatbot. The backend is complete for this, and has a temporary landing page. The project follows a JS architecture.

### static folder 

This contains static files, such as .pdfs, .txts files which can directly be downloaded if someones hits the static endpoint

### templates

This contains frontend files (if needed) like .html, .js, .css which can be used as pages for the flask app

### uploads - Resume Ranker

The Resume Ranker calls for a feature to upload a Resume, all such Resumes are uploaded here

### app.py

The main entry point of the backend server

### app-fastapi.py

The Resume Ranker uses the feature of uploading the file and getting back the ranks of the Resume across various job applications. The main `app.py` uses flask which is very slow. We use **Fast API** to make this process faster, by creating a separate endpoint for Resume Ranker.

### chatbot.py

temporary file for chatbot using python

### rankings.py

This calculates the score for the Resume using `NLP`, calls all the job descriptions from the Supabase Database, generates score, and returns them to app-fastapi.py

### readpdf.py

Temporary file to read the PDF

### resume-jobdesc.py

Temporary file to check the Resume-Job desc score

### score.py

<<<<<<< HEAD
Finds out the score, this file exists to keep the idea of calculate the score using the previous concept where the score by `TF-IDF approach and cosine similarity`, which was later replaced by `NLP` 
=======
Finds out the score, this file exists to keep the idea of calculate the score using the previous concept where the score by `TF-IDF approach and cosine similarity`, which was later replaced by `NLP` 
>>>>>>> 19c09e64ceda5a78df2765b4624657717919dbc5
