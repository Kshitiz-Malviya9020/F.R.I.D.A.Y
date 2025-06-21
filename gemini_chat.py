import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Latest model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
