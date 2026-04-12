import os
import requests
from openai import OpenAI, DefaultHttpxClient

# This specific client setup fixes the 'proxies' exception
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    http_client=DefaultHttpxClient(trust_env=False)
)

def run():
    # 1. Reset the local environment
    requests.post("http://localhost:7860/reset")
    
    # 2. Get AI decision
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[{"role": "user", "content": "Analyze the current crisis state and provide an action."}]
    )
    decision = completion.choices[0].message.content
    
    # 3. Step the environment
    requests.post("http://localhost:7860/step", json={"action": {"decision": decision}})

if __name__ == "__main__":
    run()
