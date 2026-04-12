import os
import requests
from openai import OpenAI, DefaultHttpxClient

# Bypass the buggy 'proxies' error
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    http_client=DefaultHttpxClient(trust_env=False)
)

def run():
    requests.post("http://localhost:7860/reset")
    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[{"role": "user", "content": "Pick: explore or rest."}]
    )
    decision = completion.choices[0].message.content
    requests.post("http://localhost:7860/step", json={"decision": decision})

if __name__ == "__main__":
    run()
