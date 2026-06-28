from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def extract_skills(text):
    prompt = f"""
    You are an expert ATS system.

    Extract ONLY the professional skills from the following resume.

    Rules:
    - Return ONLY valid JSON.
    - Do not explain anything.
    - Do not include markdown.
    - Remove duplicate skills.
    - Include technical skills, software tools, frameworks,
    programming languages, certifications, and domain skills.
    - Ignore soft skills like "Hardworking", "Leadership",
    "Communication", etc.

    Resume:

    {text}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )
    content = response.choices[0].message.content.strip()

    content = content.replace("```json","")
    content = content.replace("```", "")
    content = content.strip()


    try:
        skills = json.loads(content)
    except:
        skills = {"technical_skills":[]}


    return skills

def get_all_skills(data):
    all_skill = set()

    for skill in data:
        all_skill.add(skill)
    return all_skill
