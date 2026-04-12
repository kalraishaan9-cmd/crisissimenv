import os
import requests
from openai import OpenAI, DefaultHttpxClient

# Use the Hugging Face Router
API_BASE_URL = "https://router.huggingface.co/v1"
API_KEY = os.getenv("HF_TOKEN")

# Fix for the 'proxies' TypeError in Phase 2
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY,
    http_client=DefaultHttpxClient(trust_env=False) 
)

def run():
    # 1. Reset Env
    requests.post("http://localhost:7860/reset")
    
    # 2. Get LLM Decision
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[{"role": "user", "content": "Pick an action: 'explore' or 'rest'."}]
    )
    decision = completion.choices[0].message.content

    # 3. Step Env
    response = requests.post("http://localhost:7860/step", json={"decision": decision})
    print(f"Success: {response.json()}")

if __name__ == "__main__":
    run()
