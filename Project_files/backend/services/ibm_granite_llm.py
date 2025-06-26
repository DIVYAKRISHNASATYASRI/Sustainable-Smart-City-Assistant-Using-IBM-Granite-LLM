import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
BASE_URL = "https://us-south.ml.cloud.ibm.com"

def query_llm(prompt: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model_id": "granite-13b-chat",
        "input": prompt,
        "project_id": PROJECT_ID
    }
    response = requests.post(f"{BASE_URL}/v1/generate", json=payload, headers=headers)
    return response.json().get("result")