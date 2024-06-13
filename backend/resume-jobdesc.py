"""
Author : Badal Prasad Singh

Datasets used : Datasets for Resume, Resume Job Des
This .py file scores resumes based on their similarity to a given job description using the TF-IDF apprach and cosine similarity."
"""

import fitz
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(path):
    document = fitz.open(path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

text = extract_text_from_pdf("Datasets/Resume1.pdf")

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

text_preprocessed = preprocess_text(text)

def vectorize_text(texts):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    return vectors, vectorizer

def calculate_similarity(vectorized_job_desc, vectorized_resumes):
    similarities = cosine_similarity(vectorized_job_desc, vectorized_resumes)
    return similarities

def score_resumes(job_description, resume_texts):
    job_desc_cleaned = preprocess_text(job_description)
    resumes_cleaned = [preprocess_text(resume) for resume in resume_texts]

    vectors, vectorizer = vectorize_text([job_desc_cleaned]+resumes_cleaned)
    job_desc_vector = vectors[0]
    resume_vectors = vectors[1:]

    similarities = calculate_similarity(job_desc_vector, resume_vectors)
    scores = similarities[0]

    return scores

def main(job_description_path, resume_paths):
    with open("Resume Job Des/"+job_description_path, 'r') as f:
        job_description = f.read()

    resume_texts = []
    for resume_path in resume_paths:
        resume_texts.append(extract_text_from_pdf(resume_path))

    scores = score_resumes(job_description, resume_texts)

    for i, score in enumerate(scores):
        output.append(f"{job_description_path[:-4:]}: {score:.7f}/10")

output = []

if __name__ == "__main__":
    job_description_path = ["Data Scientist.txt","Software Engineer.txt", "Frontend Developer.txt", "Full Stack Developer.txt"]
    resume_paths = ["Datasets/Resume1.pdf"]
    for job_des in job_description_path:
        main(job_des, resume_paths)
    print(output)