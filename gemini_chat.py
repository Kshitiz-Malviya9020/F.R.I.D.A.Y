import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCdfwtyArKlcBpCu1npmsibrUlUpZV-TcU"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Use the latest available model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"