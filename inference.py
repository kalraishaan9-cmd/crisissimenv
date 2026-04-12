import os
import requests
from openai import OpenAI, DefaultHttpxClient

# Setup
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
API_KEY = os.getenv("HF_TOKEN")
ENV_URL = "http://localhost:7860"

# THE FIX: trust_env=False stops the 'proxies' keyword error
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY,
    http_client=DefaultHttpxClient(trust_env=False)
)

def run():
    print("Starting Phase 2 Mission...")
    # Reset
    requests.post(f"{ENV_URL}/reset")
    
    # Step: Send a simple prompt to the LLM
    chat_completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[{"role": "user", "content": "You are an agent in a simulation. Say 'I am ready'."}]
    )
    decision = chat_completion.choices[0].message.content
    
    # Send decision to your OpenEnv
    response = requests.post(f"{ENV_URL}/step", json={"decision": decision})
    print(f"Env Response: {response.json()}")

if __name__ == "__main__":
    run()
