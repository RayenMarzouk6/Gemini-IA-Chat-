import google.generativeai as genai
import os
from dotenv import load_dotenv

# Charger la clé API depuis .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configurer Gemini API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Fonction pour envoyer un message à Gemini
def get_gemini_response(user_input):
    response = model.generate_content(user_input)
    return response.text
