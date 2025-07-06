# reformatter.py
import os
import requests
from prompts import PLATFORM_PROMPTS
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

def generate_platform_outputs(article, platforms):
    outputs = {}
    for platform in platforms:
        prompt = PLATFORM_PROMPTS[platform].format(article=article)
        response = call_groq_api(prompt)
        outputs[platform] = response
    return outputs

def call_groq_api(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(GROQ_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error: {str(e)}"
