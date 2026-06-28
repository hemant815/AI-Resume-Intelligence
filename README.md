# 📄 AI Resume Analyzer + ATS Score + Career Recommendation

An AI-powered Resume Analyzer built with **Python**, **Streamlit**, **Sentence Transformers**, **Machine Learning**, and **Groq LLM**. The application analyzes resumes against job descriptions, predicts the candidate's job category, calculates an ATS compatibility score, extracts technical skills using an LLM, identifies missing skills, and recommends relevant career paths.

---

## 🚀 Features

* 📄 Upload resume in PDF format
* 📝 Paste any job description
* 🤖 Predict resume category using a Machine Learning model
* 🎯 Calculate ATS Score using semantic similarity
* 🧠 Extract technical skills using Groq LLM
* ✅ Display matched skills
* ❌ Identify missing skills
* 💼 Recommend suitable career roles
* ⚡ Fast and interactive Streamlit interface

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Sentence Transformers
* Cosine Similarity

### Large Language Model

* Groq API
* Llama-3.3-70B-Versatile

### NLP

* NLTK
* FTFY

### PDF Processing

* PyMuPDF (fitz)

### Frontend

* Streamlit

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── skills.py
├── career.py
├── models/
│   └── resume_classifier.pkl
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── screenshots/
```

---

## ⚙️ How It Works

### Step 1: Upload Resume

The user uploads a resume in PDF format.

### Step 2: Paste Job Description

The user pastes the target job description.

### Step 3: Resume Processing

The application:

* Extracts text from the PDF
* Cleans and preprocesses the text
* Tokenizes and lemmatizes the content

### Step 4: Resume Classification

A trained Machine Learning model predicts the most suitable resume category.

Examples:

* Data Science
* Machine Learning Engineer
* Frontend Developer
* Backend Developer
* DevOps Engineer
* Business Analyst

### Step 5: ATS Score Calculation

The application generates embeddings for:

* Resume
* Job Description

using the **all-mpnet-base-v2** Sentence Transformer model.

The ATS score is calculated using cosine similarity.

### Step 6: Skill Extraction

Groq LLM extracts professional skills from:

* Resume
* Job Description

The application compares both skill sets to determine:

* Matched Skills
* Missing Skills

### Step 7: Career Recommendation

Based on the predicted resume category, the application recommends suitable career roles.

---

## 📸 Screenshots

Create a **screenshots/** folder and add images such as:

```
screenshots/

home.png

ats_score.png

matched_skills.png

career_recommendation.png
```

Then display them:

```markdown
## Home Page

![Home](screenshots/home.png)

## ATS Score

![ATS](screenshots/ats_score.png)

## Skill Matching

![Skills](screenshots/matched_skills.png)
```

---

## 💻 Installation

### Clone the repository

```bash
git clone https://github.com/hemant815/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Example Workflow

1. Upload Resume
2. Paste Job Description
3. Click **ATS Score**
4. View:

   * Predicted Category
   * ATS Score
   * Matched Skills
   * Missing Skills
   * Career Recommendations

---

## 🔮 Future Improvements

* Resume improvement suggestions
* Interview question generation
* Resume summary generation
* Multi-language resume support
* OCR support for scanned resumes
* Resume ranking for recruiters
* Batch resume analysis
* Recruiter dashboard
* Docker deployment
* Cloud deployment (AWS, Azure, GCP)

---

## 📦 Requirements

* Python 3.10+
* Streamlit
* Sentence Transformers
* Scikit-learn
* NLTK
* Groq
* PyMuPDF
* Joblib
* Pandas
* python-dotenv
* FTFY

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Hemant Patel**

AI & Machine Learning Enthusiast

GitHub: https://github.com/hemant815

LinkedIn: www.linkedin.com/in/hemant-patidar-900a69300

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
