import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_quiz(text, num_questions=5):
    prompt = f"""
    You are a teacher creating a quiz. 
    From the following lecture transcript, generate {num_questions} multiple choice questions. 

    Each question must be JSON object with:
    - "question": the question text
    - "options": a list of 4 possible answers
    - "answer": the correct answer text

    Return a JSON array like this:
    [
      {{
        "question": "What is ...?",
        "options": ["A", "B", "C", "D"],
        "answer": "B"
      }}
    ]

    Transcript:
    {text}
    """
    response = model.generate_content(prompt)

    raw_output = response.text.strip()

    # Extract JSON safely
    try:
        quiz = json.loads(raw_output)
    except:
        quiz = json.loads(raw_output[raw_output.find("["): raw_output.rfind("]")+1])

    return quiz