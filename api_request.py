import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("WEATHERSTACK_API_KEY")

if not api_key:
    raise ValueError("WEATHERSTACK_API_KEY not found. Please set it in your .env file.")

api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"
