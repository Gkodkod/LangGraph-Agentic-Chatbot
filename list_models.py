"""
Run this script once to list all available Gemini models for your API key.
Usage: uv run python list_models.py
"""
import google.generativeai as genai
from config import BaseConfig

settings = BaseConfig()
genai.configure(api_key=settings.GOOGLE_API_KEY)

print("Available models:")
for m in genai.list_models():
    print(f"  {m.name}  (supported: {m.supported_generation_methods})")
