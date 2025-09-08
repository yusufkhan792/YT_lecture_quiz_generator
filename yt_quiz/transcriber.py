import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def transcribe_audio(audio_file):
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Pass audio properly as a dict
    response = model.generate_content([
        {
            "mime_type": "audio/mp3",
            "data": open(audio_file, "rb").read()
        },
        "Transcribe this audio into text."
    ])

    return response.text