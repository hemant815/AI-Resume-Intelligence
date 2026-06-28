import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
import fitz
from sklearn.metrics.pairwise import cosine_similarity

from career import recommend_career
from skills import extract_skills, get_all_skills

@st.cache_resource
def load_embed():
    embedding = SentenceTransformer("all-mpnet-base-v2")
    return embedding

@st.cache_resource
def load_model():
    model = joblib.load("models/resume_classifier.pkl")
    return model
embedding_model = load_embed()
model = load_model()

def pdf_text(pdf_path):
    text = ""
    
    if pdf_path is not None:
        # pdf_bytes = pdf_path.read()
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

        doc.close()
    return text
def clean_text(text):
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # # Keep letters, numbers, +, #, ., -, and spaces
    text = re.sub(r"[^a-zA-Z0-9+#.\-\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    #remove numbers
    text = re.sub(r"\+?\d[\d\s()-]{8,}\d", " ", text)

    return text

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    #1 tokenize
    tokens = word_tokenize(str(text))
    
    #2 stopword
    tokens = [word for word in tokens if word.lower() not in stop_words]
    #3 Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


pdf = st.file_uploader('Upload your Resume',type=['pdf'])
desc = st.text_area('Paste Job Description',height=500)
btn = st.button('ATS Score',width='stretch')
if pdf and desc and btn:
    resume_text = pdf_text(pdf)
    clean_resume_text = clean_text(resume_text)
    clean_desc = clean_text(desc)

    preprocess_resume = preprocess(clean_resume_text)
    preprocess_desc = preprocess(clean_desc)

    preprocess_resume = " ".join(preprocess_resume)
    preprocess_desc = " ".join(preprocess_desc)

    resume_embedding = embedding_model.encode(
            preprocess_resume,
            convert_to_numpy=True
        )
    desc_embedding = embedding_model.encode(
        preprocess_desc,
        convert_to_numpy=True
        )
    job = model.predict([resume_embedding])[0]
    similarity = cosine_similarity([resume_embedding],[desc_embedding])[0][0]
    ats_score = round(similarity * 100,2)
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"🎯 Predicted Category: {job}")
    with col2:
        st.metric(
            label="ATS Score",
            value=f"{ats_score}%"
        )
    resume_skills = extract_skills(preprocess_resume)
    job_skills = extract_skills(preprocess_desc)
    # cl1, cl2 = st.columns(2)
    # with cl1:
    #     for skill in set(resume_skills["technical_skills"]):
    #             st.write(skill)
    # with cl2:
    #     for skill in set(job_skills['skills']):
    #         st.write(skill)
    resume_set = get_all_skills(resume_skills['technical_skills'])
    job_set = get_all_skills(job_skills['skills'])
    matched = sorted(resume_set & job_set)

    missing = sorted(job_set - resume_set)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("✅ Matched Skills")
        for skill in matched:
            st.write(skill)

    with c2:
        st.subheader("❌ Missing Skills")
        for skill in missing:
            st.write(skill)
    career = recommend_career(job)
    st.subheader("Predicted Category")
    st.success(job)

    st.subheader("Career Recommendations")

    for c in career:
        st.write("✅", c)
    
    





