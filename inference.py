import os
import requests
from openai import OpenAI, DefaultHttpxClient

# CRITICAL: trust_env=False prevents the proxy-related crash in the validator
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    http_client=DefaultHttpxClient(trust_env=False)
)

def run():
    # 1. Reset the environment server
    try:
        requests.post("http://localhost:7860/reset", timeout=10)
    except Exception as e:
        print(f"Reset failed: {e}")

    # 2. Get the AI decision
    # If this fails, it's usually an API key (HF_TOKEN) issue
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[
            {"role": "system", "content": "You are a crisis management AI."},
            {"role": "user", "content": "Analyze the state and provide a decision."}
        ]
    )
    decision = completion.choices[0].message.content
    
    # 3. Send the action back to your FastAPI server
    try:
        requests.post(
            "http://localhost:7860/step", 
            json={"action": {"decision": decision}},
            timeout=10
        )
    except Exception as e:
        print(f"Step failed: {e}")

if __name__ == "__main__":
    run()
