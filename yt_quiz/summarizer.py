import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_text(text):
    prompt = f"Summarize the following transcript into 5-7 key bullet points:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()